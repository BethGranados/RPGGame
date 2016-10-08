from actor import *
class npc(actor):
    def __init__(self, xCord, yCord):
        actor.__init__(self,xCord, yCord)
        self.image.blit(pygame.image.load("NPC.bmp"), (0,0))
        self.image.set_colorkey((0, 128, 0))
