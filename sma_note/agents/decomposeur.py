from sma_note.agent import Agent


class Decomposeur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "Decomposeur"
        self.body.color = (100 ,100 , 100)
        self.proiesName = ["Herbivore", "Carnivore", "SuperPredateur" ]
        self.predateursNames = ["Vegetal"]
