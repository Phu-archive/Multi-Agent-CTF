from pycolab import ascii_art
from pycolab import rendering
import gym

import numpy as np
from gridworld.multiAgentEnv import MultiAgentEnvironment

class PartialObservableMultiAgentEnvironment(MultiAgentEnvironment):
    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, env_map, sprites, window_size=2):
        super().__init__(env_map, sprites)
        self.window_size = window_size

    def createWindow(self, image, middlePosition):
        pos_x = middlePosition.col
        pos_y = middlePosition.row

        left = pos_x - self.window_size + 1
        up = pos_y - self.window_size + 1
        right = pos_x + self.window_size
        down = pos_y + self.window_size

        image_y, image_x, _ = image.shape

        cropped_image = image[max(up, 0):min(image_y, down), max(left, 0):min(image_x, right), :]

        if left < 0:
            cropped_image = np.pad(cropped_image, ((0, 0), (abs(left), 0), (0, 0)), 'constant')

        if up < 0:
            cropped_image = np.pad(cropped_image, ((abs(up), 0), (0, 0), (0, 0)), 'constant')

        if right > image_x:
            cropped_image = np.pad(cropped_image, ((0, 0), (0, right - image_x), (0, 0)), 'constant')

        if down > image_y:
            cropped_image = np.pad(cropped_image, ((0, 0), (0, down - image_y), (0, 0)), 'constant')

        return cropped_image

    def extractObservations(self, fullView):
        return [self.createWindow(fullView, pos) for pos in self.playerPositions]
