"""
Author: Renato Regalado
Created: March 27, 2020
Exercise 13-5+6
Write a game that places a ship on the left side of the screen and allows the player to move the ship up and down. 
Make theship fire a bullet that travels right across the screen when the player presses spacebar.
Make sure bullets are deleted once they disappear off the screen  
"""

import os
import sys
from time import sleep
import random
import pygame



from settings import Settings
from rocket import Rocket
from lasers import Laser
from enemy import Enemy
from game_stats import GameStats
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

        #Create an instance to store game statistics
        self.stats = GameStats(self)

        #import the rocket and make an instance of it
        self.rocket = Rocket(self)
        #import the laser sprites
        self.lasers = pygame.sprite.Group()
        #import the enemy sprites
        self.enemies = pygame.sprite.Group()

        self._create_enemies()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            #watch for keyboard and mouse events
            self._check_events()
            if self.stats.game_active:
                self.rocket.update()
                self._update_lasers()
                self._update_enemy()
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
        #draw lasers
        for laser in self.lasers.sprites():
            laser.draw_laser()
        
        #draw the enemies
        self.enemies.draw(self.screen)
        #Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to keypress down events"""
        if event.key == pygame.K_w:
            #move the rocket up
            self.rocket.moving_up = True
        elif event.key == pygame.K_s:
            #move the rocket down
            self.rocket.moving_down = True
            #move the rocket to the right
        elif event.key == pygame.K_d:
            self.rocket.moving_right = True
            #move the rocket to the left
        elif event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_laser()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to keypress releases"""
        #stop moving the rocket
        if event.key == pygame.K_w:
            self.rocket.moving_up = False
        if event.key == pygame.K_s:
            self.rocket.moving_down = False
        if event.key == pygame.K_d:
            self.rocket.moving_right = False
        if event.key == pygame.K_a:
            self.rocket.moving_left = False

    def _fire_laser(self):
        """Create a new laser and add it to the lasers group"""
        if len(self.lasers) < self.settings.lasers_allowed:
            new_laser = Laser(self)
            self.lasers.add(new_laser)
        
    def _update_lasers(self):
        """Update the position of lasers and get rid of old lasers"""
        #update laser positions
        self.lasers.update()
        #Get rid of bullets that have disappeared
        for laser in self.lasers.copy():
            if laser.rect.left >= self.rocket.screen_rect.right:
                self.lasers.remove(laser)
        
        self._check_laser_enemy_collisons()
    
    def _create_enemies(self):
        """Create an enemy ship"""
        enemy_number = random.randint(1,5)
        for _ in range(enemy_number):
            enemy = Enemy(self)
            enemy.rect.y = random.randint(1, self.settings.screen_height)
            self.enemies.add(enemy)
            
    def _update_enemy(self):
        """move the enemy to the left"""
        self.enemies.update()
        for enemy in self.enemies.copy():
            if enemy.rect.right <= 0:
                self.enemies.remove(enemy)
        
        #look for enemy-rocket collision
        if pygame.sprite.spritecollideany(self.rocket, self.enemies):
            self._rocket_hit()
    
    def _check_laser_enemy_collisons(self):
        #check for any lasers that have hit enemies
        #if so get rid of the alien and the bullet
        collisions = pygame.sprite.groupcollide(self.lasers, self.enemies, True, True)

        if not self.enemies:
            #destroy lasers and create a new fleet.
            self.lasers.empty()
            self._create_enemies()
    
    def _rocket_hit(self):
        if self.stats.rockets_left > 0:
            #decreaset the remaining rockets
            self.stats.rockets_left -= 1
            #get rid of any remaining
            self.enemies.empty()
            self.lasers.empty()

            #Pause
            sleep(0.5)

            #restore the ship
            self.rocket.center_rocket()
            self._create_enemies()
        
        else:
            self.stats.game_active = False

if __name__ == '__main__':
    #Make a game instance, and then run the game
    SR = SidewaysRocket()
    SR.run_game()