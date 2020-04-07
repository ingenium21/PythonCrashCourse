"""import pygame module"""
import pygame
from pygame.sprite import Sprite

class Orb(Sprite):
    """A Class to manage the orb fired from the ship"""

    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.orb_color

        self.rect = pygame.Rect(0, 0, self.settings.orb_width, self.settings.orb_height)
        self.rect.midleft = tp_game.rocketShip.rect.midright

        #create the orb rect (0,0) and then set the correct position
        self.x = float(self.rect.x)

    def update(self):
        """move the orb across the screen"""
        #update the decimal position of the laser
        self.x += self.settings.orb_speed
        #update the rect position
        self.rect.x = self.x
    
    def draw_orb(self):
        """draw the orb to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)