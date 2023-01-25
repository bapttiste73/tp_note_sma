import random

import core
from sma_note.item import Item

class Vegetal(Item):
    def __init__(self, positionX=None, positionY=None):
        super().__init__(positionX, positionY)
        self.name = "Vegetal"
        self.color = (0, 255, 0) # vert

        #Une plante a un niveau qui représente sa taille, plus le niveau est haut plus il nourrit
        #Les plantes grandissent avec le temps
        self.size = 2
        self.age = 0
        self.cycle = random.randint(core.memory('scenario')["Vegetal"]["parametres"]["cycle"][0],core.memory('scenario')["Vegetal"]["parametres"]["cycle"][1])
        self.level = 100

        self.predateursNames = ["Herbivore"]

    def update(self):
        self.age += 1
        if(self.age % self.cycle == 0):
            self.age = 0
            self.grow()
    def grow(self):
        if(self.level < 500):
            self.level += 100
            self.size += 2