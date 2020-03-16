"""
Author: Renato Regalado
Created: March 16, 2020
Exercise 12-2
Find an image of a game character, place it in the center of the screen
and match the background color of the image to the background of the screen.
"""
import os
import sys
import pygame
from marius import Marius

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

class BlueSky:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")

        #set the background color
        self.bg_color = (66, 158, 245)

        self.marius = Marius(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
            self.marius.blitme()

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run it
    bs = BlueSky()
    bs.run_game()