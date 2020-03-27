import os

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH) #this is used so that my game runs in the correct directory


class Settings:
    """A class to store all settings for Rocket Game"""

    def __init__(self):
        """initialize the game's settings"""
        #screen Settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (32, 32, 32)

        #rocket settings
        self.rocket_speed = 1

        #Bullet Settings
        self.laser_speed = 1.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (0, 255, 255)
        self.lasers_allowed = 3