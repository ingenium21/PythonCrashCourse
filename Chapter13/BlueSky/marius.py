"""Import pygame"""
import pygame


class Marius:
    """A Class to manage Marius"""

    def __init__(self, bs_game):
        """Initialize Marius and set his starting position"""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        #Load the mario image and get its rect
        self.image = pygame.image.load('images/mario1.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        
        #start every new mario at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

