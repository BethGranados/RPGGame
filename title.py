from actor import *

class title(actor):
    def __init__(self, xCord, yCord):
        actor.__init__(self, xCord, yCord)
        self.size = (400, 150)
        self.image = pygame.Surface(self.size).convert()
        self.image.blit(pygame.image.load("mainMenu.bmp"), (0,0))
