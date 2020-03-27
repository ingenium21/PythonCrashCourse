"""import pygame module"""
import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """A class to manage the lasers fired from the ship"""

    def __init__(self, sr_game):

        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings
        self.color = self.settings.laser_color

        #Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.laser_width, self.settings.laser_height)
        self.rect.midright = sr_game.rocket.rect.midright

        #Store the bullets position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the laser across the screen"""
        #update the decimal position of the laser
        self.x += self.settings.laser_speed
        #update the rect position
        self.rect.x = self.x
    
    def draw_laser(self):
        """Draw the laser to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)