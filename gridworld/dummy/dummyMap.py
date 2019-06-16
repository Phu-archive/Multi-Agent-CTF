from gridworld.map_art import EnvMap
"""
#: Is wall/ maze
' ' is open space 
'A' is player one team one 
'B' is player two team one 
'C' is player one team two 
'D' is player two team two 
'$' is flag
'1' is base one
'2' is base two 
"""
GAME_ART = ['#############',
            '# A   #  1  #',
            '#     #  B  #',
            '#     #     #',
            '#           #',
            '#     #     #',
            '### $ ##### #',
            '#     #     #',
            '#     #     #',
            '#           #',
            '# D   #     #',
            '# 2   # C   #',
            '#############']

COLOR_MAP = {'#': (0, 0, 0), ' ': (1, 1, 1), 'A': (1, 0, 0),'B': (1, 0, 0), 'C':(0, 0, 1), 'D':(0, 0, 1), '$': (0, 1, 0), '1': (1, 1, 0), '2': (0, 1, 1)}

dummyMap = EnvMap(GAME_ART, COLOR_MAP)
