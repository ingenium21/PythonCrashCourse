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
from time import sleep

from settings import Settings
from rocketShip import RocketShip
from target import Target
from orb import Orb
from button import Button
from game_stats import GameStats

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

        #create an instance to store game statistics
        self.stats = GameStats(self)

        #import the rocket ship and make an instance of it
        self.rocketShip = RocketShip(self)

        #import the orb
        self.orbs = pygame.sprite.Group()

        #import the target
        self.target = Target(self)

        #Create a play button
        self.play_button = Button(self, "Play")

        #misses
        self.miss = 0
    
    def run_game(self):
        while True:
            #watch for keyboard and mouse events
            self._check_events()
            if self.stats.game_active:
                self.rocketShip.update()
                self._update_target()
                self._update_orbs()
            self._update_screen()
    
    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        
        #draw the rocket ship
        self.rocketShip.blitme()

        #draw the target
        self.target.blitme()

        for orb in self.orbs.sprites():
            orb.draw_orb()
        
        #draw the play button
        if not self.stats.game_active:
            self.play_button.draw_button()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_keydown_events(self, event):
        """Respond to keypress events"""
        if event.key == pygame.K_w:
            #move the rocket up
            self.rocketShip.moving_up = True
        elif event.key == pygame.K_s:
            #move the rocket down
            self.rocketShip.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_orb()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.rocketShip.moving_up = False
        if event.key == pygame.K_s:
            self.rocketShip.moving_down = False
    
    def _update_target(self):
        """move the target up and down"""
        self.target.update()

    def _fire_orb(self):
        """update the position of the orb"""
        new_orb = Orb(self)
        self.orbs.add(new_orb)
        
    
    def _update_orbs(self):
        """update the position of the orbs and get rid of old orbs"""
        #update the orb positions
        self.orbs.update()

        #Get rid of old orbs that have disappeared
        for orb in self.orbs.copy():
            if orb.rect.left >= self.rocketShip.screen_rect.right:
                self.orbs.remove(orb)
                self.miss += 1

        #look for orb-target collision
        if pygame.sprite.spritecollideany(self.target, self.orbs):
            self._target_hit()
        
        if self.miss >= 3:
            self.stats.game_active = False
    
    def _target_hit(self):
        #render GOAL! on screen
        self.target.shorten_target()
        self.miss = 0

        #self.stats.game_active = False
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        """start the game"""
        #reset the game statistics
        self.stats.reset_stats()
        self.miss = 0
        self.stats.game_active = True

        #Get rid of any remaining shots
        self.orbs.empty()

        #Center the target and ship
        self.target.center_target()
        self.rocketShip.center_rocketShip

if __name__ == '__main__':
    #Make a game instance, and then run the game
    TP = TargetPractice()
    TP.run_game()