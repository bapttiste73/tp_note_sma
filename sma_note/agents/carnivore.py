from sma_note.agent import Agent


class Carnivore(Agent):
    SEUIL_MANGER = 20
    def __init__(self, body):
        super().__init__(body)
        self.name = "Carnivore"
        self.body.color = (255, 255, 0)
        self.proiesName = ["Herbivore"]
        self.predateursNames = ["SuperPredateur", "Decomposeur"]
        self.comportement = None

    def update(self):
        super().update()
        pass;

