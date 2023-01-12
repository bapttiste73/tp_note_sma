import datetime

import core
from sma_note.agents.decomposeur import Decomposeur
from sma_note.body import Body


class bodyDecomposeur(Body):
    def __init__(self, ):
        super().__init__()
        self.name="Decomposeur"

        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,1000)

    def dedouble(self):
        bodyClone = type(self)()

        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y
        core.memory('agents').append(Decomposeur(bodyClone))