from src.environment.hollow_knight_env import HollowKnightEnv
from src.agent.ppo_agent import train_with_checkpoints

def main():
    env = HollowKnightEnv()
    model = train_with_checkpoints(env, total_timesteps=1000000, checkpoint_interval=100000)
    model.save("hollowknight_model_final")

if __name__ == "__main__":
    main()