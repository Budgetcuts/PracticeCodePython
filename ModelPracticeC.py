import bullet

class GUI:
    def __init__(self, width = 640, height =480):
        self.screen = pygame.display.set_moode((width,height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.hero = Hero.hero()
        self.sprites = pygame.sprite.Group((self.hero))
