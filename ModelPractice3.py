import pygame
import random

class Bullets(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        #initialize all the spirte functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bullet.png')
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.direction = direction
        if (self.direction == "right"):
            self.image = pygame.transform.flip(self.image, True, False)
        #center in order to get the bullets to fire from the middle of the character
        # Bullet((hero.centerx, hero,centery)) would be the initialization of the object
    def update(self):
        if direction == "right":
            self.rect.centerx += 10
        else:
            self.rect.centerx -= 10
