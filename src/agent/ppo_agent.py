from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

class TensorboardCallback(BaseCallback):
    def __init__(self, verbose=0):
        super(TensorboardCallback, self).__init__(verbose)
    
    def _on_step(self) -> bool:
        self.logger.record('reward', self.training_env.get_attr('reward')[0])
        return True

def train_agent(env, total_timesteps=1000000):
    model = PPO("CnnPolicy", env, verbose=1, tensorboard_log="./hollowknight_tensorboard/")
    model.learn(total_timesteps=total_timesteps, callback=TensorboardCallback())
    return model