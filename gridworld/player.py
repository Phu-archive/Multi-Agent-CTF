from pycolab.prefab_parts import sprites as prefab_sprites
from gridworld.utils import Reward
import numpy as np

class Player(prefab_sprites.MazeWalker):

    """
    Simple Player Controller

    Args:
        playerNum (int) -- The id of the player (MUST HAVE)
    """

    def __init__(self, corner, position, character):
        super().__init__(corner, position, character, impassable='#')
        if not hasattr(self, "playerNum"):
            raise ValueError("playerNum Has to be specified. Did you put it after super().__init__ ?")

        if not isinstance(self.playerNum, int):
            raise TypeError("Player Number has to be integer")

    def update(self, actions, board, layers, backdrop, things, the_plot):
        """
        Mostly dealt with Normal Action/Movement of the agents (clockwise direction)
            - 0 is north
            - 1 is east
            - 2 is south
            - 3 is west
        """
        del layers, backdrop, things

        if isinstance(actions, list) or isinstance(actions, tuple) or isinstance(actions, np.ndarray):
            action = actions[self.playerNum]
        else:
            action = None

        if action == 0:
            self._north(board, the_plot)
        elif action == 1:
            self._east(board, the_plot)
        elif action == 2:
            self._south(board, the_plot)
        elif action == 3:
            self._west(board, the_plot)
        elif action is not None:
            raise ValueError("Action Not Found the possible actions are [0, 1, 2, 3]")

        self.behavior(
            action, board, the_plot
        )

    def behavior(self, action, board, the_plot):
        """
        This will define how the reward will be given the game dynamics etc.

        Args:
            action (int) -- The agent's action
            board (np.array) -- The board representation
            the_plot -- Reference to game object (we can terminate episode/add reward)
        """
        raise NotImplementedError

    def __str__(self):
        return f"Player_{self.playerNum}"

    def __repr__(self):
        return f"Player_{self.playerNum}"

    def assignReward(self, the_plot, reward):
        """
        Instead of doing complex namedtuple and list via the_plot.add_reward()
        we can just do a simple wrapper (make things easier) and cleaner.

        Args:
            the_plot -- The representation/reference of the environment
            reward (float) -- The received reward for the agent
        """

        if not(isinstance(reward, float) or isinstance(reward, int)):
            raise ValueError("The reward should be float or integer")

        the_plot.add_reward([
            Reward(agentNum=self.playerNum, reward=reward)
        ])
