from gridworld.player import Player
from gridworld.utils import Reward

has_flag = False

class PlayerSprite(Player):
    def __init__(self, corner, position, character, player_num = 0, team = 1):
        self.playerNum = player_num

        # team A
        self.team = team
        self.flag = False
        super().__init__(corner, position, character)

    def behavior(self, actions, board, the_plot):
        """
        Assign a reward if agent is back in base (1) and has flag.
        """
        global has_flag
        print(f"Player Num: {self.playerNum} Has {chr(board[self.position])}")

        if ord(str(self.team)) == board[self.position]:
        # if ord(str(self.team)) == board[self.position] and self.flag:
            self.assignReward(the_plot, 100.0)
            self.flag = False
             # no one can pick up flag
            has_flag = self.flag

            # NEED TO ADD: return flag to spawn point

            # #Assign reward to ally also
            # the_plot.add_reward([
            # Reward(agentNum=1, reward=100.0)
            #  ])
        # Pick Up Flag
        elif ord('$') == board[self.position] and not has_flag: # can't pick up flag unless its available
            self.flag = True
            has_flag = self.flag
            self.assignReward(the_plot, 0.0)
            # NEED TO ADD: work out how to remove the flag from the board when this happens until its returned.
        else:
            self.assignReward(the_plot, 0.0)

class PlayerSprite1(PlayerSprite):
    def __init__(self, corner, position, character):
        super().__init__(corner, position, character, player_num = 0, team = 1)

class PlayerSprite2(PlayerSprite):
    def __init__(self, corner, position, character):
        super().__init__(corner, position, character, player_num = 1, team = 1)

class PlayerSprite3(PlayerSprite):
    def __init__(self, corner, position, character):
        super().__init__(corner, position, character, player_num = 2, team = 2)

class PlayerSprite4(PlayerSprite):
    def __init__(self, corner, position, character):
        super().__init__(corner, position, character, player_num = 3, team = 2)
