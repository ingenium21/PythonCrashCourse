"""Import pygame"""
import pygame
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path) #this is used so that my game runs in the correct directory

class Rocket:
    """A class to manage the rocket"""

    def __init__(self, rg_game):
        """Initialize the rocket and set its starting position"""
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        #movement flags
        self.moving_up = False
        self.moving_down = False

        #Load the rocket image and get its rect
        self.image = pygame.image.load('Images/cohete_off.png')
        self.rect = self.image.get_rect()

        #Start each new rocket at the center of the screen
        self.rect.midleft = self.screen_rect.midleft

        #Store a decimal value of the rocket's horizontal position
        self.y = float(self.rect.y)
    
    def update(self):
        """Update the rocket's position based on the movement flags"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        
        #update rect object from self.x and self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at it's current location"""
        self.screen.blit(self.image, self.rect)