import datetime
import random

import core
from sma_note.agents.herbivore import Herbivore
from sma_note.body import Body


class bodyHerbivore(Body):
    def __init__(self, ):
        super().__init__()
        self.name="Herbivore"
        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,random.randint(core.memory('scenario')["Herbivore"]["parametres"]["esperanceVie"][0],core.memory('scenario')["Herbivore"]["parametres"]["esperanceVie"][1]))

        self.vitesseMax = random.randint(core.memory('scenario')["Herbivore"]["parametres"]["vitesseMax"][0],core.memory('scenario')["Herbivore"]["parametres"]["vitesseMax"][1])
        self.accelMax = random.randint(core.memory('scenario')["Herbivore"]["parametres"]["accelMax"][0],core.memory('scenario')["Herbivore"]["parametres"]["accelMax"][1])

        self.maxFaim = random.randint(core.memory('scenario')["Herbivore"]["parametres"]["maxFaim"][0],core.memory('scenario')["Herbivore"]["parametres"]["maxFaim"][1])
        self.maxFatigue = random.randint(core.memory('scenario')["Herbivore"]["parametres"]["maxFatigue"][0],core.memory('scenario')["Herbivore"]["parametres"]["maxFatigue"][1])
        self.maxReproduction = random.randint(core.memory('scenario')["Herbivore"]["parametres"]["maxReproduction"][0],core.memory('scenario')["Herbivore"]["parametres"]["maxReproduction"][1])

        self.niveauFaim = 0
        self.niveauFatigue = 0
        self.niveauReproduction = random.randint(0, self.maxReproduction)

        #Score genetique
        self.geneticScore = self.vitesseMax + self.accelMax + self.maxFaim + self.maxFatigue + self.maxReproduction
    def reproduction(self):
        bodyClone = type(self)()

        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y

        core.memory('agents').append(Herbivore(bodyClone))

        #Ajout d'un deuxième enfant pour les herbivores
        bodyClone2 = type(self)()

        bodyClone2.position.x = self.position.x
        bodyClone2.position.y = self.position.y
        core.memory('agents').append(Herbivore(bodyClone2))
