import sys
import pygame

class BlueSky:
    """Overall class to manage assets and behavior"""

    def __init__(self):
        """initialize the game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")

        #set the background color
        self.bg_color = (66, 158, 245)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run it
    bs = BlueSky()
    bs.run_game()