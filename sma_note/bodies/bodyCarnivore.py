import datetime

import core
from sma_note.agents.carnivore import Carnivore
from sma_note.body import Body


class bodyCarnivore(Body):
    def __init__(self):
        super().__init__()
        self.name="Carnivore"
        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,10)
        self.accelMax = 3

    def dedouble(self):
        bodyClone = type(self)()

        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y
        core.memory('agents').append(Carnivore(bodyClone))
