"""importing necessary libaries"""
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to represent a single enemy in the game"""
    def __init__(self, sr_game):
        """initialize the enemy and set its starting position"""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings

        #Load the enemy image and sets its rect attribute.
        self.image = pygame.image.load('images/enemy.png')
        self.image = pygame.transform.scale(self.image, (55, 54))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        #set star rect at top left position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save exact position of star
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the enemy at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Move the enemy to the left """
        self.x -= self.settings.enemy_speed
        self.rect.x = self.x