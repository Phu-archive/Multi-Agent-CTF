from gridworld.map_art import EnvMap

GAME_ART_flagreward =  ['#######',
                        '# 1 A #',
                        '#   $ #',
                        '#######']

COLOR_MAP_flagreward = {'#': (0, 0, 0), ' ': (1, 1, 1), 'A': (1, 0, 0), '$': (0, 1, 0), '1': (1, 1, 0)}

testMap1 = EnvMap(GAME_ART_flagreward, COLOR_MAP_flagreward)

GAME_ART = ['#########',
            '#   B1  #',
            '#       #',
            '#    A  #',
            '#########']

COLOR_MAP = {'#': (0, 0, 0), ' ': (1, 1, 1), 'A': (1, 0, 0),'B': (0, 0, 1), '$': (0, 1, 0), '1': (1, 1, 0)}

twoMap = EnvMap(GAME_ART, COLOR_MAP)
