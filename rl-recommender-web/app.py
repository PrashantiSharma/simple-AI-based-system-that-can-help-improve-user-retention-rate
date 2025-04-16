from flask import Flask, request, jsonify, render_template
import numpy as np
from stable_baselines3 import PPO
import json
import os

app = Flask(__name__)

# Load trained model
model_path = "models/agent_RL"
if not os.path.exists(model_path + ".zip"):  # Check for .zip extension
    print(f"Warning: Model file '{model_path}.zip' not found. Ensure your model is saved correctly.")
    # You might want to handle this error more gracefully in a production environment
    model = None
else:
    model = PPO.load(model_path)

action_list = [
    ('discount', 10, 'email', 'immediate'),
    ('discount', 15, 'sms', 'immediate'),
    ('free_shipping', 0, 'email', 'next_day'),
    ('free_shipping', 0, 'push', 'immediate')
]
@app.route('/')  # Add this route
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if model is None:
        return jsonify({"error": "Model not loaded."}), 500

    user_data = request.json

    # Validate user data to prevent KeyError
    required_keys = [
        'recency', 'frequency', 'monetary_value', 'engagement_score',
        'discount_sensitive', 'free_shipping_preferred', 'email_opens',
        'sms_response', 'push_response', 'last_purchase_days'
    ]
    if not all(key in user_data for key in required_keys):
        return jsonify({"error": "Missing required user features."}), 400

    try:
        # Convert to state vector
        state = np.array([
            user_data['recency'],
            user_data['frequency'],
            user_data['monetary_value'],
            user_data['engagement_score'],
            float(user_data['discount_sensitive']),
            float(user_data['free_shipping_preferred']),
            user_data['email_opens'],
            user_data['sms_response'],
            user_data['push_response'],
            user_data['last_purchase_days']
        ], dtype=np.float32).reshape(1, -1)

        # Get recommendation
        action, _ = model.predict(state)
        recommendation = action_list[action[0]]

        return jsonify({
            "recommendation": recommendation,
            "user_features": user_data
        })

    except KeyError as e:
        return jsonify({"error": f"Missing key in user data: {e}"}), 400
    except IndexError:
        return jsonify({"error": "Invalid action index from the model."}), 500
    except Exception as e:
        print(f"Error during recommendation: {e}")
        return jsonify({"error": "An unexpected error occurred during recommendation."}), 500
    pass

if __name__ == '__main__':
    app.run(debug=True)