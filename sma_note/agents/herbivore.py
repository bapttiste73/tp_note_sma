from sma_note.agent import Agent


class Herbivore(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "Herbivore"
        self.body.color = (0, 255, 255)
        self.proiesName = ["Vegetal"]
        self.predateursNames = ["Carnivore", "SuperPredateur"]