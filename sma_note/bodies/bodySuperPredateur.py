import datetime

import core
from sma_note.agents.superPredateur import SuperPredateur
from sma_note.body import Body


class bodySuperPredateur(Body):
    def __init__(self, ):
        super().__init__()
        self.name="SuperPredateur"

        self.esperanceVie = self.dateNaissance + datetime.timedelta(0,15)

    def dedouble(self):
        bodyClone = type(self)()
        print('ok')
        bodyClone.position.x = self.position.x
        bodyClone.position.y = self.position.y
        core.memory('agents').append(SuperPredateur(bodyClone))