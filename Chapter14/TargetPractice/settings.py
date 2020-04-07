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

        #orb Settings
        self.orb_speed = 1.0
        self.orb_width = 55
        self.orb_height = 54
        self.orb_color = (0, 255, 255)
        self.orbs_allowed = 3

        #target settings
        self.target_speed = 0.5
        self.target_width = 25
        self.target_height = 200
        self.target_color = (255, 255, 255)