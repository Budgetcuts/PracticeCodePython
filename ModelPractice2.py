import pygame
import random

class Hero(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.strenght = random.rand.range(10)
        self.intel = random.randrange(10)
        self.speed = random.randrange(10)

    def move(self, direction):
        if(direction.lower = "down")
            self.rect.y += self.speed
        if(direction.lower = "up")
            self.rect.y -= self.speed
        if(direction.lower = "left")
            self.rect.y -= self.speed
        if(direction.lower = "right")
            self.rect.y += self.speed

    def fight(self,other):
        if (other.strength > self.strength):
            return False
        else:
            return random.choice([True,False])
