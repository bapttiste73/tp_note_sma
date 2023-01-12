from sma_note.agent import Agent


class Vegetal(Agent):
    def __init__(self, body):
        super().__init__(body)
        self.name = "Vegetal"
        self.body.color = (0, 255, 0)
        self.body.maxSpeed = 2
        self.body.maxForce = 0.1