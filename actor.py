import pygame

class actor:
    size = (32, 32)
    cord = (40, 40)
    def __init__(self, xCord, yCord):
        self.cord = (xCord, yCord)
        self.image = pygame.Surface(self.size).convert()
        self.passable = True
    def display(self):
        return self.image
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
        return selfpassable
