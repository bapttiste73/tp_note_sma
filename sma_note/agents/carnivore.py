from sma_note.agent import Agent


class Carnivore(Agent):
    SEUIL_MANGER = 20
    def __init__(self, body):
        super().__init__(body)
        self.name = "Carnivore"
        self.body.color = (255, 255, 0) # jaune
        self.proiesNames = ["Herbivore"]
        self.predateursNames = ["SuperPredateur"]
        self.amisNames = []


