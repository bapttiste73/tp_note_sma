import datetime
import random

import core
from sma_note.agents.superPredateur import SuperPredateur
from sma_note.body import Body


class bodySuperPredateur(Body):
    def __init__(self, ):
        super().__init__()
        self.name="SuperPredateur"

        self.vitesseMax = random.randint(core.memory('scenario')["SuperPredateur"]["parametres"]["vitesseMax"][0],core.memory('scenario')["SuperPredateur"]["parametres"]["vitesseMax"][1])
        self.accelMax = random.randint(core.memory('scenario')["SuperPredateur"]["parametres"]["accelMax"][0],core.memory('scenario')["SuperPredateur"]["parametres"]["accelMax"][1])

        self.maxFaim = random.randint(core.memory('scenario')["SuperPredateur"]["parametres"]["maxFaim"][0],core.memory('scenario')["SuperPredateur"]["parametres"]["maxFaim"][1])
        self.maxFatigue = random.randint(core.memory('scenario')["SuperPredateur"]["parametres"]["maxFatigue"][0],core.memory('scenario')["SuperPredateur"]["parametres"]["maxFatigue"][1])
        self.maxReproduction = random.randint(core.memory('scenario')["SuperPredateur"]["parametres"]["maxReproduction"][0],core.memory('scenario')["SuperPredateur"]["parametres"]["maxReproduction"][1])

        self.niveauFaim = random.randint(0, self.maxFaim)
        self.niveauFatigue = random.randint(0, self.maxFatigue)
        self.niveauReproduction = random.randint(0, self.maxReproduction)



    def reproduction(self):
        bodyClone = type(self)()
        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y
        print("SP" + str(self.niveauReproduction))

        core.memory('agents').append(SuperPredateur(bodyClone))