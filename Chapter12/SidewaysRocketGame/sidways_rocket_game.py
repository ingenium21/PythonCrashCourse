"""
Author: Renato Regalado
Created: March 27, 2020
Exercise 12-6
Write a game that places a ship on the left side of the screen and allows the player to move the ship up and down. 
Make theship fire a bullet that travels right across the screen when the player presses spacebar.
Make sure bullets are deleted once they disappear off the screen  
"""

import os
import sys
import pygame
from settings import Settings
from rocket import Rocket

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH) #this is used so that my game runs in the correct directory

class SidewaysRocket:
    """overrall class to manage assets and behavior"""

    def __init__(self):
        """intialize the game, and create resources"""
        pygame.init()
        self.settings = Settings()

        #Sets the window size and caption
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Rocket Game")

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
        if event.key == pygame.K_UP:
            #move the rocket up
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            #move the rocket down
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to keypress releases"""
        #stop moving the rocket
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

if __name__ == '__main__':
    #Make a game instance, and then run the game
    SR = SidewaysRocket()
    SR.run_game()