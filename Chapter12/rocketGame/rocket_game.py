"""
Author: Renato Regalado
Created: March 19, 2020
Exercise 12-4
Make a game that begins with a rocket at the center of the screen.  Allow the player
to move the rocket up, down, left, or right using the four arrow keys.  Make sure 
the rocket never moves beyond any edge of the screen.  
"""
import os
import sys
import pygame
from settings import Settings
from rocket import Rocket

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path) #this is used so that my game runs in the correct directory

class RocketGame:
    """overrall Class to manage assets and behavior"""

    def __init__(self):
        """initialize the game, and create resources"""
        pygame.init()
        self.settings = Settings()

        #Sets the window size and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")

        #import the rocket and make an instance of it
        self.rocket = Rocket(self)
    
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            #watch for keyboard and mouse events
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        #draw the rocket
        self.rocket.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to keypress down events"""
        if event.key == pygame.K_RIGHT:
            #Move the rocket to the right
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move the rocket to the left
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            #move the rocket up
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            #move the rocket down
            self.rocket.moving_down = True
    
    def _check_keyup_events(self, event):
        """Respond to keypress releases"""
        #stock moving the rocket
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

if __name__ == '__main__':
    #Make a game instance, and then run the game
    RG = RocketGame()
    RG.run_game()