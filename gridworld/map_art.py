# Wrapper class for the Map. might be useful to have adjustable maze

class EnvMap(object):
    def __init__(self, game_art, color_map):
        self.game_art = game_art
        self.color_map = color_map
