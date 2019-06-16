from pycolab import ascii_art
from pycolab import rendering
import gym

from gridworld.multiAgentEnv import MultiAgentEnvironment

class FullObservableMultiAgentEnvironment(MultiAgentEnvironment):
    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, env_map, sprites):
        super().__init__(env_map, sprites)

    def extractObservations(self, observation):
        return [observation] * self.num_player
