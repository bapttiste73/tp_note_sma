import datetime
import random

import core
from sma_note.agents.decomposeur import Decomposeur
from sma_note.body import Body
from sma_note.items.mineral import Mineral
from sma_note.items.vegetal import Vegetal


class bodyDecomposeur(Body):
    def __init__(self, ):
        super().__init__()
        self.name="Decomposeur"

        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,100)

        self.vitesseMax = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["vitesseMax"][0],core.memory('scenario')["Decomposeur"]["parametres"]["vitesseMax"][1])
        self.accelMax = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["accelMax"][0],core.memory('scenario')["Decomposeur"]["parametres"]["accelMax"][1])

        self.maxFaim = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxFaim"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxFaim"][1])
        self.maxFatigue = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxFatigue"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxFatigue"][1])
        self.maxReproduction = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxReproduction"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxReproduction"][1])

        self.niveauFaim = random.randint(0, self.maxFaim)
        self.niveauFatigue = random.randint(0, self.maxFatigue)
        self.niveauReproduction = random.randint(0, self.maxReproduction)


    #Un décomposeur ne peut pas se reproduire mais il libére des elements mineralisés
    def reproduction(self):
        pass
        # if self.niveauReproduction >= self.maxReproduction:
        #     # core.memory('items').append(Mineral(self.position.x, self.position.y))

