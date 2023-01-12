
import core
from body import Body
from sma_note.agents.carnivore import Carnivore
from sma_note.agents.superPredateur import SuperPredateur
from sma_note.agents.decomposeur import Decomposeur
from sma_note.agents.herbivore import Herbivore
from sma_note.bodies.bodyCarnivore import bodyCarnivore
from sma_note.bodies.bodyDecomposeur import bodyDecomposeur
from sma_note.bodies.bodyHerbivore import bodyHerbivore
from sma_note.bodies.bodySuperPredateur import bodySuperPredateur


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [600, 600]

    core.memory("agents", [])
    core.memory("item", [])

    for i in range(0, 5):
        core.memory('agents').append(SuperPredateur(bodySuperPredateur()))

    for i in range(0, 10):
        core.memory('agents').append(Carnivore(bodyCarnivore()))

    for i in range(0, 30):
        core.memory('agents').append(Herbivore(bodyHerbivore()))

    for i in range(0,5):
        core.memory('agents').append(Decomposeur(bodyDecomposeur()))



    print("Setup END-----------")

def defineLife(b):
    for a in core.memory('agents'):
        if a.uuid != b.uuid:
            if a.body.position.distance_to(b.body.position) < 10:
                if a.name in b.predateursNames:
                    a.estMort = True
                    b.vientDeManger = True

                if b.name in a.predateursNames:
                    b.estMort = True
                    a.vientDeManger = True

def computePerception(agent):
        agent.body.fustrum.perceptionList = []
        for b in core.memory('agents'):
            if agent.uuid != b.uuid:
                if agent.body.fustrum.inside(b.body):
                    agent.body.fustrum.perceptionList.append(b.body)
        for b in core.memory('item'):
            if agent.body.fustrum.inside(b):
                agent.body.fustrum.perceptionList.append(b)
        pass;


def computeDecision(agent):
    agent.update()

def applyDecision(agent):
    agent.body.update()



def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)


core.main(setup, run)
