"""
Author: Renato Regalado
Created: March 27, 2020
Exercise 14-2
Create a rectangle at the right edge of the screen that moves up and down at a steady rate.
Then have a ship appear on the left side of the screen that the player can move up and down while firing bullets at the moving, rectangular target.
Add a Play button that starts the game, and when the player misses the target three times, end the game and make the Play button reappear.  
Let the player restart the game with this play button.
"""
import os
import sys
import pygame

from settings import Settings
from rocketShip import RocketShip
PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH) #this is used so that my game runs in the correct directory


class TargetPractice:
    """Overrall class to manage assets and behavior"""

    def __init__(self):
        """intialize the game, and create resources"""
        pygame.init()
        self.settings = Settings()

        #Set the window size and caption
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        #import the rocket ship and make an instance of it
        self.rocketShip = RocketShip(self)
    
    def run_game(self):
        while True:
            #watch for keyboard and mouse events
            self._check_events()
            self.rocketShip.update()
            self._update_screen()
    
    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        
        #draw the rocket ship
        self.rocketShip.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypress events"""
        if event.key == pygame.K_w:
            #move the rocket up
            self.rocketShip.moving_up = True
        elif event.key == pygame.K_s:
            #move the rocket down
            self.rocketShip.moving_down = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.rocketShip.moving_up = False
        if event.key == pygame.K_s:
            self.rocketShip.moving_down = False

if __name__ == '__main__':
    #Make a game instance, and then run the game
    TP = TargetPractice()
    TP.run_game()