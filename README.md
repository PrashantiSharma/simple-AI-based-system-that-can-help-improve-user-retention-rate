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
