import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Create environment
env = gym.make("LunarLander-v2", render_mode="rgb_array")

def main():
    mode = input('Train or Load? ').lower()

    if mode == 'train':
        # Instantiate the agent
        # model = PPO("MlpPolicy", env, verbose=1)
        model = PPO.load("ppo_lunar", env=env)
        # Train the agent and display a progress bar
        model.learn(total_timesteps=int(2e5), progress_bar=True)
        # Save the agent
        model.save("ppo_lunar")
        del model  # delete trained model to demonstrate loading
    elif mode == 'load':
        # Load the trained agent
        # NOTE: if you have loading issue, you can pass `print_system_info=True`
        # to compare the system on which the model was trained vs the current one
        # model = DQN.load("dqn_lunar", env=env, print_system_info=True)
        model = PPO.load("ppo_lunar", env=env)

        # Evaluate the agent
        # NOTE: If you use wrappers with your environment that modify rewards,
        #       this will be reflected here. To evaluate with original rewards,
        #       wrap environment in a "Monitor" wrapper before other wrappers.
        mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

        # Enjoy trained agent
        vec_env = model.get_env()
        obs = vec_env.reset()
        for i in range(2e5):
            action, _states = model.predict(obs, deterministic=True)
            obs, rewards, dones, info = vec_env.step(action)
            vec_env.render("human")
    else:
        print('Sorry, I did not understand that.')
        main()

main()