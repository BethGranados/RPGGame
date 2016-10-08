import pygame
from actor import *

class gameViewObj:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Scrolling")
        self.size = [640, 640]
        self.screen = pygame.display.set_mode(self.size)
        self.frameClock = pygame.time.Clock()
        self.cameraCords = [800, 400]
        self.fps = 60
    def paint(self, actor):
        loc = actor.location()
        dispLoc = (loc[0] - self.cameraCords[0], loc[1] - self.cameraCords[1])
        self.screen.blit(actor.display(), dispLoc) 
    def render(self, actorList, amount):
        for x in range (0, amount):
            self.paint(actorList[x])
    def outBoundsLeft(self, actor, buff = 0):
        if (actor.location()[0] + actor.sizing()[0] + buff)  > (self.cameraCords[0] + self.size[0]):
            return True
        return False
    def outBoundsRight(self, actor, buff = 0):
        if (actor.location()[0] - buff)  < (self.cameraCords[0]):
            return True
        return False
    def outBoundsTop(self, actor, buff = 0):
        if (actor.location()[1] + actor.sizing()[1] + buff)  > (self.cameraCords[1] + self.size[1]):
            return True
        return False
    def outBoundsBottom(self, actor, buff = 0):
        if (actor.location()[1] - buff)  < (self.cameraCords[1]):
            return True
        return False
    def scroll(self, horizontal, vertical):
        self.cameraCords = (self.cameraCords[0] + horizontal, self.cameraCords[1] + vertical)
    def loadLevel(self, location):
        with open(location) as fileInfo:
            level=fileInfo.read()
        return level
    def flippingYouOff(self):
        pygame.display.flip()
        self.frameClock.tick(self.fps)
        self.screen.fill([0,0,0])
    def gameScreen(self):
        return self.screen
    def copy(self, otherViewObj):
        self.screen.blit(otherViewObj.gameScreen(), (0,0))
