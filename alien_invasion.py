import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import pygame

class AlienInvasion:
    def __init__(self):
        # to run in fullscreen mode see 283 self.screen adjustments
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            print(len(self.bullets))
            self._update_screen()
            

    def _check_events(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                   self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                   self._check_keyup_events(event)
                        
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        self.bullets.update()
        # delete unused bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()