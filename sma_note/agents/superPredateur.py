from sma_note.agent import Agent


class SuperPredateur(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "SuperPredateur"
        self.body.color = (255, 0, 0)
        self.proiesName = ["Carnivore"]
        self.predateursNames = ["Decomposeur"]

