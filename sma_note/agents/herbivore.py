from sma_note.agent import Agent
from sma_note.body import Body
from sma_note.item import Item


class Herbivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "Herbivore"
        self.body.color = (0, 255, 255) # cyan
        self.proiesNames = ["Vegetal"]
        self.predateursNames = ["Carnivore"]
        self.amisNames = ["SuperPredateur"]

    def filtrePerception(self):
        proies = []
        predateurs = []
        amis = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)

            if isinstance(i, Item) and i.name == "Vegetal":
                if i.name in self.proiesNames:
                    proies.append(i)
            if isinstance(i, Body) and i.estMort == False:
                if i.name in self.predateursNames and i.dort == False: #Si le predateur est en train de dormir, il ne peut pas manger et on en a pas peur
                    predateurs.append(i)
                if i.name in self.amisNames:
                    amis.append(i)


        proies.sort(key=lambda x: x.dist, reverse=False)
        predateurs.sort(key=lambda x: x.dist, reverse=False)
        amis.sort(key=lambda x: x.dist, reverse=False)

        return proies, predateurs, amis