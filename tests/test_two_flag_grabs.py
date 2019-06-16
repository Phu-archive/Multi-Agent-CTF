from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from gridworld.fullObsEnv import FullObservableMultiAgentEnvironment
from gridworld.dummy.dummyPlayer import PlayerSprite1, PlayerSprite2, PlayerSprite3, PlayerSprite4
from gridworld.dummy.testMaps import twoMap

import matplotlib.pyplot as plt

import pytest

# @pytest.fixture
def init_values():
    NUM_PLAYERS  = 2
    NUM_ACTIONS = 4

    env = FullObservableMultiAgentEnvironment(
        twoMap,
        {'A': PlayerSprite1, 'B': PlayerSprite2},
    )

    return NUM_PLAYERS, NUM_ACTIONS, env

def test_flags_example(init_values):
    """
    Mostly dealt with Normal Action/Movement of the agents (clockwise direction)
        - 0 is north
        - 1 is east
        - 2 is south
        - 3 is west
    """

    NUM_PLAYERS, NUM_ACTIONS, env = init_values

    obs, _, _ = env.reset()
    actions = [[2,3],[2,1],[0,0],[0,0],[3,3]]
    expected_rewards_0 = [0, 0, 0, 0, 0]
    expected_rewards_1 = [0, 0, 0, 100, 0]

    for i in range(5):

        current_action = actions[i]

        obs, reward, done = env.step(current_action)
        assert expected_rewards_0[i]==reward[0].reward
        assert expected_rewards_1[i]==reward[1].reward

test_flags_example(
    init_values()
)
