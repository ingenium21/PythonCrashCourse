class Settings:
    """A class to store all settings for Rocket Game"""

    def __init__(self):
        """initialize the game's settings"""
        #screen Settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (32, 32, 32)

        #rocket settings
        self.rocket_speed = 1