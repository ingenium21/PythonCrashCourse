"""Import pygame"""
import pygame
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path) #this is used so that my game runs in the correct directory

class RocketShip:
    """A class to manage the rocket ship"""
    
    def __init__(self, tp_game):
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()

        #movement flags
        self.moving_up = False
        self.moving_down = False

        #Load the rocket image and get its rect
        self.image = pygame.image.load('Images/rocketShip.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 55))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        #Start each new rocket at the center of the screen
        self.rect.midleft = self.screen_rect.midleft

        #Store a decimal value of the rocket's horizontal position
        self.y = float(self.rect.y)
    
    def update(self):
        """Update the rocket ship's position based on the movement flags"""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        #update rect object from self.x and self.y
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the rocket ship at it's current location"""
        self.screen.blit(self.image, self.rect)
    
    def center_rocketShip(self):
        """Center the rocket ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)