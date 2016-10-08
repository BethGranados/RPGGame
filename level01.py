from actor import *
from gameViewObj import *
from player import *
from NPC import *
from title import *
from backgroundObj import *

class level01:
    def mainLoop(self):
        self.scene = gameViewObj()
        levelDat = self.scene.loadLevel("town.txt")
        self.nextState = 01
        self.sceneList = []
        self.sceneAmnt = 0
        row = 0
        col = 0

        #loads the game level.
        for count in range(0, len(levelDat)):
            if levelDat[count] == '\n':
                row += 1
                col = 0
            else:
                self.sceneList.append(backgroundOb(col * 32, row * 32, levelDat[count]))
                self.sceneAmnt +=1
                col += 1

        #Loads the actors
        self.actorList = [player(900, 500), npc(300, 300)]
        self.amount = 2
        self.running = True

        #Game loop
        while self.running:
            self.events()
            self.update()
            self.scene.render(self.sceneList, self.sceneAmnt)
            self.scene.render(self.actorList, self.amount)
            self.scene.flippingYouOff()
        return self.nextState
                    
    #All actions
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actorList[0].changeDirX(-5)
                    self.actorList[0].changeCharDir(2)
                if event.key == pygame.K_RIGHT:
                    self.actorList[0].changeDirX(5)
                    self.actorList[0].changeCharDir(3)
                if event.key == pygame.K_DOWN:
                    self.actorList[0].changeDirY(5)
                    self.actorList[0].changeCharDir(0)
                if event.key == pygame.K_UP:
                    self.actorList[0].changeDirY(-5)
                    self.actorList[0].changeCharDir(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.actorList[0].changeDirX(0)
                if event.key == pygame.K_RIGHT:
                    self.actorList[0].changeDirX(0)
                if event.key == pygame.K_DOWN:
                    self.actorList[0].changeDirY(0)
                if event.key == pygame.K_UP:
                    self.actorList[0].changeDirY(0)
    #Make changes to all actors.   
    def update(self):
        for x in range(1, self.sceneAmnt):
            self.actorList[0].canMove(self.sceneList[x])
        self.actorList[0].move()
        if(self.scene.outBoundsLeft(self.actorList[0], 20)):
           self.scene.scroll(5, 0)
        if(self.scene.outBoundsRight(self.actorList[0], 20)):
           self.scene.scroll(-5, 0)
        if(self.scene.outBoundsTop(self.actorList[0], 20)):
           self.scene.scroll(0, 5)
        if(self.scene.outBoundsBottom(self.actorList[0], 20)):
           self.scene.scroll(0, -5)
