import core
from sma_note.agent import Agent
from sma_note.body import Body
from sma_note.items.vegetal import Vegetal


class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "Decomposeur"
        self.body.color = (100 ,100 , 100) # gris
        self.proiesNames = ["Herbivore", "Carnivore", "SuperPredateur"]
        self.predateursNames = []
        self.amisNames = []

    #Le décomposeur ne mange que les animaux morts
    def filtrePerception(self):
        proies = []
        predateurs = []
        amis = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Body):
                if i.name in self.proiesNames and i.estMort == True:
                    proies.append(i)

        proies.sort(key=lambda x: x.dist, reverse=False)

        return proies, predateurs, amis

    def update(self):
        super().update()
        if self.body.estMort:
            core.memory('items').append(Vegetal(self.body.position.x, self.body.position.y))
            core.memory('agents').remove(self)