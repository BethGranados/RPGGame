from actor import *

class player(actor):
    cord = (100, 100)
    movement = (0, 0)
    def __init__(self, xCord, yCord):
        actor.__init__(self, xCord, yCord)
        self.size = (32, 32)
        self.image = [ pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert()]
        self.image[0].blit(pygame.image.load("PlayerF.bmp"), (0,0))
        self.image[1].blit(pygame.image.load("PlayerB.bmp"), (0,0))
        self.image[2].blit(pygame.image.load("PlayerL.bmp"), (0,0))
        self.image[3].blit(pygame.image.load("PlayerR.bmp"), (0, 0))
        self.image[0].set_colorkey((0, 128, 0))
        self.image[1].set_colorkey((0, 128, 0))
        self.image[2].set_colorkey((0, 128, 0))
        self.image[3].set_colorkey((0, 128, 0))
        self.num = 0
    def move(self):
        self.cord = (self.cord[0] + self.movement[0], self.cord[1] + self.movement[1])
    def changeDirX(self, x):
        self.movement = (x, self.movement[1])
    def changeDirY(self, y):
        self.movement = (self.movement[0], y)
    def changeCharDir(self, dirNum):
        self.num=dirNum
    def display(self):
        return self.image[self.num]
    def canMove(self, otherActor):
        if otherActor.isPassable():
            return
        if ((self.cord[0] + self.size[0] + self.movement[0]) < otherActor.cord[0]) or ((self.cord[1] + self.movement[1]) > (otherActor.cord[1] + otherActor.size[1])) or((self.cord[1] + self.size[1] + self.movement[1]) < otherActor.cord[1]) or ((self.cord[0] + self.movement[0]) > (otherActor.cord[0] + otherActor.size[0])):
         return
        else:
            self.movement = (0, 0)
            return
