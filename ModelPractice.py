import pygame

class MainCharacter:
    def __init__(self, name, image, positionX, positionY, strength, speed, intelligence):
        self.name = name
        self.image = image
        self.positionX = positionX
        self.positionY = positionY
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

    def move(self):
        while(pygame.KEYDOWN):
            if (pygame.K_DOWN):
                self.positionY +=1
            if (pygame.K_UP):
                self.positionY -=1
            if (pygame.K_RIGHT):
                self.positionX +=1
            if (pygame.K_LEFT):
                self.positionX -=1
    def fight(self):
        Fight = True
        x = randrange(0,2)
        if (x > 0):
            Fight = True
        else:
            Fight = False
        return Fight
