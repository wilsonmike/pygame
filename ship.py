import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.x += .5
        if self.moving_left:
            self.rect.x += .5
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)