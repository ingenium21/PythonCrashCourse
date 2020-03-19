"""Import pygame"""
import pygame

class Rocket:
    """A class to manage the rocket"""

    def __init__(self, rg_game):
        """Initialize the rocket and set its starting position"""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #Load the rocket image and get its rect
        self.image = pygame.image.load('Images/cohete_off.png')
        self.rect = self.image.get_rect()

