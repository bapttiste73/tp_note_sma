import datetime

import core
from sma_note.agents.herbivore import Herbivore
from sma_note.body import Body


class bodyHerbivore(Body):
    def __init__(self, ):
        super().__init__()
        self.name="Herbivore"

        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,3)

    def dedouble(self):
        bodyClone = type(self)()

        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y
        core.memory('agents').append(Herbivore(bodyClone))