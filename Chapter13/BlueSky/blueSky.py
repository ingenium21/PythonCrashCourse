"""
Author: Renato Regalado
Created: April 1, 2020
Exercise 13-3
Find an image of a raindrop and create a grid of raindrops.  Make the raindrops fall toward the bottom
of the screen until they disappear.
"""
import os
import sys
import pygame
import random
from marius import Marius
from raindrops import Raindrop

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)

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
        self.rain = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_Screen()


    
    def _update_Screen(self):
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        #draw the rain
        self.rain
        self.marius.blitme()
        #Make the most recently drawn screen visible
        pygame.display.flip()
    
    def _create_rain(self):
        """Create a bunch of raindrops to make rain"""
        raindrop = Raindrop(self)
        raindrop.rect.x = random.randint(1, 800)
        self.rain.add(raindrop)

    def _update_rain(self):
        """move the rain downward"""
        self.raindrop.update()
        for raindrop in self.rain.copy():
            if raindrop.rect.top >= 600:
                self.rain.remove(raindrop)


if __name__ == '__main__':
    #Make a game instance and run it
    bs = BlueSky()
    bs.run_game()