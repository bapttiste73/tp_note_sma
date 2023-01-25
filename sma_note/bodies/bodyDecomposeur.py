import datetime
import random

import core
from sma_note.body import Body


class bodyDecomposeur(Body):
    def __init__(self, ):
        super().__init__()
        self.name="Decomposeur"

        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["esperanceVie"][0],core.memory('scenario')["Decomposeur"]["parametres"]["esperanceVie"][1]))

        self.vitesseMax = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["vitesseMax"][0],core.memory('scenario')["Decomposeur"]["parametres"]["vitesseMax"][1])
        self.accelMax = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["accelMax"][0],core.memory('scenario')["Decomposeur"]["parametres"]["accelMax"][1])

        self.maxFaim = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxFaim"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxFaim"][1])
        self.maxFatigue = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxFatigue"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxFatigue"][1])
        self.maxReproduction = random.randint(core.memory('scenario')["Decomposeur"]["parametres"]["maxReproduction"][0],core.memory('scenario')["Decomposeur"]["parametres"]["maxReproduction"][1])

        self.niveauFaim = 0
        self.niveauFatigue = 0
        self.niveauReproduction = random.randint(0, self.maxReproduction)

        self.geneticScore = 0

    def reproduction(self):
        pass

