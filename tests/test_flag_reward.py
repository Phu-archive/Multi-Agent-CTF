from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import copy
import matplotlib.pyplot as plt

from gridworld.fullObsEnv import FullObservableMultiAgentEnvironment
from gridworld.dummy.dummyPlayer import PlayerSprite1
from gridworld.dummy.testMaps import testMap1

from gridworld.utils import num_action_to_name

import pytest

"""
Use this to test out features, such as rewards and or agents killing
"""

@pytest.fixture
def init_values():
    NUM_ACTIONS = 4

    env = FullObservableMultiAgentEnvironment(
        testMap1,
        {'A': PlayerSprite1},
    )
    return NUM_ACTIONS, env

def test_rendering_reward(init_values):

    NUM_ACTIONS, env = init_values

    obs, _, _ = env.reset()
    all_obs = []
    I = 3
    actions = []

    current_action = []
    actions = [3, 3, 1, 1, 2, 0, 3, 3, 3]
    rewards = []
    expected_rewards = [0.0]*7 + [100.00] + [0.0]

    for i in range((I ** 2)):

        current_action = [actions[i]]
        obs, reward, done = env.step(current_action)
        all_obs.append(copy.deepcopy(obs[0]))
        rewards.append(reward[0])
        actions.append(current_action)

        assert expected_rewards[i]==reward[0].reward

    fig, axs = plt.subplots(nrows=I, ncols=I, figsize=(obs[0].shape[0], obs[0].shape[1]),
                            subplot_kw={'xticks': [], 'yticks': []})

    for i, (ax, grid, act) in enumerate(zip(axs.flat, all_obs, actions)):
        ax.imshow(grid)
        ax.set_title('Step: ' + str(i + 1) + ' Action: (' + ', '.join([num_action_to_name[act]]) + ')' + ' Reward: '+str(rewards[i].reward))

    plt.tight_layout()
    plt.show()
