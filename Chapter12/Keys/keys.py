"""
Author: Renato Regalado
Created: March 16, 2020
Exercise 12-5
Keys: Make a Pygame file that creates an empty screen.  In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected
Run the program and press various keys to see how Pygame responds
"""
import os
import sys
import pygame

PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(PATH)


class Keys: 
    """overrall class to manage assets and behavior"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Keys")

        #Set the background color
        self.bg_color = (66, 158, 245)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event)
            
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            #MAke the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run it
    k = Keys()
    k.run_game()