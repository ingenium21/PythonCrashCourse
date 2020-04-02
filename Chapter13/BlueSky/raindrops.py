"""Import pygame"""
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, bs_game):
        """Models raindrop object"""
        super().__init__()
        self.screen = bs_game.screen
        # self.screen_rect = bs_game.get_rect()

        #Load the rain image and get its rect
        self.image = pygame.image.load('images/raindrop.png').convert()
        self.image = pygame.transform.scale(self.image, (55, 54))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        #Start each new raindrop near the top left of the screenj.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the raindrop's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #star speed
        self.star_speed = 10

    def blitme(self):
        """draw the raindrop at its current position"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Move the raindrop down """
        self.y += self.star_speed
        self.rect.y = self.y