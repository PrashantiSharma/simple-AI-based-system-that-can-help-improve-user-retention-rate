# Reinforcement Learning Recommendation Agent

A reinforcement learning-based recommendation system that delivers personalized offers to e-commerce users based on their behavior, preferences, and engagement patterns.

## Overview

This project uses a custom Gym environment and the PPO algorithm (via Stable-Baselines3) to train an agent that learns which offers to send to users in order to maximize engagement and conversions.

## Features

- Customizable action space (offer type, value, channel, timing)
- Rich state features based on user behavior
- Modular and extensible architecture
- Easy-to-use training and inference scripts

## Project Structure

- `data/`: Raw and processed user behavior data
- `models/`: Saved trained agent
- `src/`: Source code (environment, training, inference)
- `notebooks/`: Data exploration and feature engineering
- `requirements.txt`: Dependency list

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt

Here's a professional `README.md` for your GitHub repository that documents your RL recommendation agent project:

```markdown
# Reinforcement Learning Recommendation Agent

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Stable-Baselines3](https://img.shields.io/badge/Stable%20Baselines3-1.7.0-red)
![Gymnasium](https://img.shields.io/badge/Gymnasium-0.28.1-lightgrey)

An RL-powered recommendation system that generates personalized offers for e-commerce users.

## 📁 Repository Structure

```
rl-recommendation-agent/
├── data/
├── models/
├── notebooks/
└── requirements.txt/
```

##  Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**:
   ```bash
   python src/train.py --data data/user_behavior.xlsx --save models/ppo_recommender
   ```

3. **Generate recommendations**:
   ```bash
   python src/recommend.py --model models/ppo_recommender.pth --user_id 42
   ```

## Model Details

**Algorithm**: Proximal Policy Optimization (PPO)  
**Action Space**: 144 possible combinations of:
- Offer types (discount/free shipping/recommendation/bundle)
- Values (5/10/15)
- Channels (email/sms/push)
- Timing (immediate/delay_1hour/delay_6hours)

**State Features**:
1. Recency (days since last activity)
2. Frequency (total sessions)
3. Monetary value (purchase history proxy)
4. Engagement score
5. Discount sensitivity
6. Free shipping preference
7-9. Channel responsiveness (email/sms/push)
10. Days since last purchase

## Data Pipeline

1. **Raw Data** (`user_behavior.xlsx`):
   - User sessions with timestamps
   - Actions (view/add_to_cart/purchase)
   - Product categories
   - Channels

2. **Feature Engineering**:
   - RFM (Recency/Frequency/Monetary) metrics
   - Engagement scoring
   - Channel preference modeling
   - Behavioral clustering

## Customization

To adapt for your use case:

1. Modify the action space in `environment.py`:
   ```python
   self.action_list = [
       (offer_type, value, channel, timing)
       for offer_type in ['discount', ...]
       # ... your combinations ...
   ]
   ```

2. Adjust reward calculation:
   ```python
   def _calculate_reward(self, action_idx):
       # Implement your business rules
       if action_matches_preference:
           return high_reward
       return base_reward
   ```

## Sample Output

Recommendation for User 123:
```
State Features:
- Recency: 2.00 days
- Frequency: 8 sessions
- Monetary Value: $142.50
- Engagement Score: 0.82
- Discount Sensitive: Yes
- Preferred Channel: email

Recommended Action:
15% discount via email (immediate delivery)
```


