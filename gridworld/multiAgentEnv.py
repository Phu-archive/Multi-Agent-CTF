from pycolab import ascii_art
from pycolab import rendering
import gym

import numpy as np

class MultiAgentEnvironment(gym.Env):
    """
    Multi-Agent Environments Abstract Class

    Args:
        env_map (EnvMap) -- The environment object of the game
        sprites (dictionary key: char, value: Player) -- Mapping between character
            in the game_art to the controllable agent
        num_player (int) -- Number of player in the game
        renderer (ObservationToArray) -- Object that turns the observation to pixel
            given the color map
        current_frame (np.array) -- Current Render of the Environments (might
            be useful for video recording)
        has_flag - control if an agent can pick up a flag
    """

    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, env_map, sprites):
        self.game_art = env_map.game_art
        self.color_map = env_map.color_map
        self.sprites = sprites

        self.num_player = len(sprites)

        self.renderer =  rendering.ObservationToArray(self.color_map, dtype=float, permute=(1, 2, 0))
        self.current_frame = None



    @property
    def playersList(self):
        """
        Getting all the player in the order of the id of player (which should
            always be integer)

        Returns:
            list_of_player (list of player) -- the list of all player objects
        """
        return sorted([i for i in self.game.things.values()], key=lambda x: x.playerNum)

    @property
    def playerPositions(self):
        """
        Getting all the player position in the order of the id of players

        Returns:
            player_positions (list of position) -- the list of player positions
        """
        return list(map(lambda x: x.position , self.playersList))


    def extractObservations(self, fullView):
        """
        Given the fullView of the environment

        Args:
            fullView (np.array) -- the full observation of the environment.

        Returns:
            list of observations (list in the size of number of players)
                -- List that correspond to each agent's observation.
        """
        raise NotImplementedError


    def reset(self):
        # Just Create the New Game
        self.game = ascii_art.ascii_art_to_game(
                        self.game_art,
                        what_lies_beneath=' ',
                        sprites=self.sprites
                    )
        obs, reward, discount = self.game.its_showtime()
        obs_numpy = self.renderer(obs)
        self.current_frame = obs_numpy
        return self.extractObservations(obs_numpy), reward, self.game.game_over


    def step(self, actions):
        if len(actions) != self.num_player:
            raise ValueError("Number of Action should be equal to Number of Player")

        if self.game.game_over:
            self.game = None
            raise ValueError("The game is already ended")

        if self.game is None:
            raise ValueError("Seem Like the Environments hasn't been reseted")

        obs, reward, discount = self.game.play(actions)
        obs_numpy = self.renderer(obs)
        self.current_frame = obs_numpy

        return self.extractObservations(obs_numpy), reward, self.game.game_over

    def render(self, mode='rgb_array', close=False):
        if mode == 'rgb_array':
            return self.current_frame
        else:
            super(MyEnv, self).render(mode=mode)
