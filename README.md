# Capture The Flag Gridworld

This repository contains the implementation of multi-agent capture the flag in 2D, gridworld. Based on `pycolab`

## Basic APIs
The api for the environment is quite simple, since it is similar to OpenAI's `gym`. For now we assume fully-observability (yes, the CTF will be in partial observability)

After creating the environment

```python
env = FullObservableMultiAgentEnvironment(
    GAME_ART,
    {'P': PlayerSprite1, 'Q':PlayerSprite2},
    COLOR_MAP
)
```

We can run the environment by inputing a list

```python
obs, reward, done = env.reset()
obs, reward, done = env.step([3, 1])
```

where each entries corresponds to action of each agent in this case player number 0 playing action 3, and player number 2 playing action 1, which will get out reward in a list of tuple, which indicates which agents got, which reward.

```python
[(1, 0.0), (0, 100.0)]
```

---

For the Partial Observable Multi-Agent Environment (the window size is given) and all the same API

```python
env = PartialObservableMultiAgentEnvironment(
    GAME_ART,
    {'P': PlayerSprite1, 'Q':PlayerSprite2},
    COLOR_MAP,
    window_size=3
)
```

## Adding/Specify Player Behavior

In order to create the game, we will have to define the behavior of the players first (by using our normal controller -- Player)

```python
class PlayerSprite2(Player):
    def __init__(self, corner, position, character):
        self.playerNum = 1
        super().__init__(corner, position, character)

    def behavior(self, actions, board, the_plot):
        if ord('$') == board[self.position]:
            self.assignReward(the_plot, 100.0)
        else:
            self.assignReward(the_plot, 0.0)
```
In this case, we have to always assign the player sprite a number (MUST starting from 0)
so that we can order agent for observation output.
All agents that inherited the `Player` class will have to following action

 * Action 0 --  Up
 * Action 1 --  Right
 * Action 2 --  Down
 * Action 3 --  Left

`behavior` method is used to define how the reward is assigned and when the game will ends
(might also has a control over the dynamic of the game)

The agent, in the above example, gets reward 100 (tuple arrange in the term of player_num(tag) and reward)
if it touches `'$'` on the map, and every step reward is zero

### Tests

To run tests on picking up flag and returning to base, and receiving reward run
Test two players grabbing flag at the same time

```python
pytest testes
```

Hacking Here:
```python
# Hack to allow absolute import from the root folder
if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "gridworld"
```
