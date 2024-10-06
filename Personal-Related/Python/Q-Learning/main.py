import numpy as np
import random

############ // Q-Learning - Modelless Objective: Keeping steering at 0 while it is being pushed // ############

# Steering parameters
STEERING_MIN = -1.0
STEERING_MAX = 1.0
THRESHOLD = 0.8  # Game over if steering goes beyond

num_states = 20
try: Q = np.load('savefile')
except: Q = np.zeros((20, 3))

# Discretize steering into states (bins)
steering_bins = np.linspace(STEERING_MIN, STEERING_MAX, num_states)

# Hyperparameters
gamma = 0.9   # Discount factor
alpha = 0.1   # Learning rate
epsilon = 0.8 # Exploration rate
episodes = 1000 # Total number of episodes to train

actions = [-0.1, 0, 0.1]

# Function to get the closest state for a steering value
def get_steering_state(steering_value):
    return np.digitize(steering_value, steering_bins) - 1  # returns index of closest bin

# Function to simulate the next steering value based on action
def step(steering, action):
    new_steering = steering + action * 0.1  # Adjust steering by 0.1 units
    new_steering = np.clip(new_steering, STEERING_MIN, STEERING_MAX)  # Keep steering in bounds

    # Check game over condition (if steering exceeds threshold)
    if abs(new_steering) >= THRESHOLD:
        reward = -10  # Heavy penalty for exceeding threshold
        done = True   # Game over
    else:
        reward = 1  # Positive reward for staying in bounds
        done = False
    return new_steering, reward, done

# Q-learning algorithm
for episode in range(episodes):
    # Start at a random steering value within the safe zone
    steering = random.uniform(-THRESHOLD, THRESHOLD)

    # Run until game over
    done = False
    while not done:
        state = get_steering_state(steering)

        # Choose an action (epsilon-greedy)
        if random.uniform(0, 1) < epsilon:
            # Explore: choose a random action
            action = random.choice(actions)
        else:
            # Exploit: choose the action with the highest Q-value
            action = actions[np.argmax(Q[state, :])]

        # Take the action and observe the new state and reward
        new_steering, reward, done = step(steering, action)
        new_state = get_steering_state(new_steering)

        # Update the Q-value using the Q-learning formula
        Q[state, actions.index(action)] += alpha * (
            reward + gamma * np.max(Q[new_state, :]) - Q[state, actions.index(action)]
        )

        # Update the steering for the next step
        steering = new_steering

np.save('savefile', Q)
print("Trained Q-table:")
print(Q)

# Testing the steering agent
def run_test():
    steering = random.uniform(-THRESHOLD, THRESHOLD)
    print(f"Initial steering: {steering:.2f}")

    steps = 0
    done = False
    while not done and steps < 20:
        state = get_steering_state(steering)
        action = actions[np.argmax(Q[state, :])]  # Choose the best action
        steering, _, done = step(steering, action)
        print(f"Step {steps + 1}: Steering = {steering:.2f}")
        steps += 1

        if done:
            print("Game Over! Steering exceeded threshold.")

run_test()