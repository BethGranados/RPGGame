import pygame
class backgroundOb:
    def __init__(self, xCord, yCord, x):
        self.cord = (xCord, yCord)
        self.passable = True
        self.image = [ pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(),pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert(), pygame.Surface(self.size).convert()]
        self.image[0].blit(pygame.image.load("grass.bmp"), (0,0))
        self.image[1].blit(pygame.image.load("water.bmp"), (0,0))
        self.image[2].blit(pygame.image.load("tallGrass.bmp"), (0,0))
        self.image[3].blit(pygame.image.load("path.bmp"), (0, 0))


        self.image[4].blit(pygame.image.load("wall01.bmp"), (0,0))
        self.image[5].blit(pygame.image.load("wall02.bmp"), (0,0))
        self.image[6].blit(pygame.image.load("wall05.bmp"), (0,0))
        self.image[7].blit(pygame.image.load("shrubbery.bmp"), (0,0))

        self.image[8].blit(pygame.image.load("roof.bmp"), (0,0))
        self.image[9].blit(pygame.image.load("roof2.bmp"), (0,0))
        self.image[10].blit(pygame.image.load("roof3.bmp"), (0,0))
        self.image[11].blit(pygame.image.load("door.bmp"), (0,0))
        self.image[12].blit(pygame.image.load("rock.bmp"), (0,0))
        self.image[13].blit(pygame.image.load("bridge.bmp"), (0,0))
        self.image[14].blit(pygame.image.load("bridge02.bmp"), (0,0))

        
        if (x == '0'):
            self.num = 0
        if (x == '1'):
            self.num = 1
            self.passable = False
        if (x == '2'):
            self.num = 2
        if (x == '3'):
            self.num = 3
        if (x == '4'):
            self.num = 4
            self.passable = False
        if (x == '5'):
            self.num = 5
            self.passable = False
        if (x == '6'):
            self.num = 6
            self.passable = False
        if (x == '7'):
            self.num = 7
            self.passable = False
        if (x == '8'):
            self.num = 8
            self.passable = False
        if (x == '9'):
            self.num = 9
            self.passable = False
        if (x == 'a'):
            self.num = 10
            self.passable = False
        if (x == 'b'):
            self.num = 11
        if (x == 'c'):
            self.num = 12
            self.passable = False
        if (x == 'd'):
            self.num = 13
        if (x == 'e'):
            self.num = 14
    def display(self):
        return self.image[self.num]
    def location(self):
        return self.cord
    def sizing(self):
        return self.size
    def collide(self, otherActor):
        if ((self.cord[0] + self.size[0]) < otherActor.cord[0]) or (self.cord[1] > (otherActor.cord[1] + otherActor.size[1])) or((self.cord[1] + self.size[1]) < otherActor.cord[1]) or (self.cord[0] > (otherActor.cord[0] + otherActor.size[0])):
         return False
        else:
         return True
    def isPassable(self):
        return self.passable
