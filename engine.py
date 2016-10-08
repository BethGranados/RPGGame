from level01 import *
from mainMenu import *

class engine:
    def __init__(self):
        self.FIRSTLEVEL = 0
        self.EXITING = 1
        self.gameState = 0

        while True:
        
            if self.gameState == self.FIRSTLEVEL:
                level = level01()
                self.gameState = level.mainLoop()
            if self.gameState == self.EXITING:
                    break

