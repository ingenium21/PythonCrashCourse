"""importing the necessary libraries"""
import pygame
import random

class Target:
    """A class to represent the target in the game"""
    def __init__(self, tp_game):
        """Initialize the target and set its starting position"""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.target_color
        self.screen_rect = tp_game.screen.get_rect()

        #movement flags
        self.moving_up = False
        self.moving_down = False
        #Create a target rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.target_width, self.settings.target_height)
        
        #start the target at the center right of the screen
        self.rect.midright = self.screen_rect.midright

        #store a decimal value of the targets's vertical position
        self.y = float(self.rect.y)

    def update(self):
        """move the target up and down"""
        if not self.moving_up and not self.moving_down:
            if random.randint(0,1) == 1:
                self.moving_up = True
            else:
                self.moving_down = True
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.target_speed
        elif self.moving_up and self.rect.top <= self.screen_rect.top:
            self.moving_up = False
            self.moving_down = True
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.target_speed
        elif self.moving_down and self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
            self.moving_up = True
        
        #update rect object from self.y
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the target at its current location"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def center_target(self):
        """Center the target on the screen"""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
    
    def shorten_target(self):
        """make the target smaller"""
        self.rect = self.rect.inflate(0, -1)