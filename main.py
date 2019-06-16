from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses
import sys
import copy

import matplotlib.pyplot as plt
import numpy as np

from pycolab import ascii_art
from pycolab import rendering

from gridworld.fullObsEnv import FullObservableMultiAgentEnvironment
from gridworld.dummy.dummyPlayer import PlayerSprite1, PlayerSprite2, PlayerSprite3, PlayerSprite4
from gridworld.dummy.dummyMap import dummyMap

from gridworld.utils import num_action_to_name

NUM_PLAYERS  = 4
NUM_ACTIONS = 4

env = FullObservableMultiAgentEnvironment(
    dummyMap,
    {'A': PlayerSprite1, 'B': PlayerSprite2, 'C': PlayerSprite3, 'D': PlayerSprite4},
)

def main(argv=()):
    del argv

    obs, _, _ = env.reset()
    all_obs = []
    I = 3
    actions = []

    for i in range((I ** 2)):
        current_action = np.random.randint(0, NUM_ACTIONS, NUM_PLAYERS)
        # current_action = [0]*NUM_PLAYERS

        obs, reward, done = env.step(current_action)
        all_obs.append(copy.deepcopy(obs[0]))
        print(reward)
        actions.append(current_action)

    fig, axs = plt.subplots(nrows=I, ncols=I, figsize=(obs[0].shape[0], obs[0].shape[1]),
                            subplot_kw={'xticks': [], 'yticks': []})

    for i, (ax, grid, act) in enumerate(zip(axs.flat, all_obs, actions)):
        ax.imshow(grid)
        ax.set_title('Step: ' + str(i + 1) + ' Action: (' + ', '.join([num_action_to_name[a] for a in act]) + ')')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main(sys.argv)
