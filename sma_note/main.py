import json

import core
from sma_note.agents.carnivore import Carnivore
from sma_note.agents.superPredateur import SuperPredateur
from sma_note.agents.decomposeur import Decomposeur
from sma_note.agents.herbivore import Herbivore
from sma_note.items.vegetal import Vegetal
from sma_note.bodies.bodyCarnivore import bodyCarnivore
from sma_note.bodies.bodyDecomposeur import bodyDecomposeur
from sma_note.bodies.bodyHerbivore import bodyHerbivore
from sma_note.bodies.bodySuperPredateur import bodySuperPredateur

def setup():
    print("Setup START---------")

    f = open("scenario.json")
    data = json.load(f)
    core.memory("scenario", data)
    f.close()

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("items", [])

    for i in range(0, 2):
        core.memory('agents').append(SuperPredateur(bodySuperPredateur()))

    for i in range(0, 4):
        core.memory('agents').append(Carnivore(bodyCarnivore()))

    for i in range(0, 2):
        core.memory('agents').append(Herbivore(bodyHerbivore()))

    for i in range(0, 20):
        core.memory('agents').append(Decomposeur(bodyDecomposeur()))

    for i in range(0, 20):
        core.memory('items').append(Vegetal())

    print("Setup END-----------")

def updateEnvironment():
    for a in core.memory('agents'):
        for b in core.memory('agents'):
            if a.uuid != b.uuid:
                if a.body.position.distance_to(b.body.position) < 10:
                    if a.name in b.predateursNames:
                        a.body.vientDeManger = True
                        b.body.estMort = True

def computePerception(agent):
    agent.body.fustrum.perceptionList = []
    for b in core.memory('agents'):
        if agent.uuid != b.uuid and agent.body.fustrum.inside(b.body):
            if agent.name == "Decomposeur":
                agent.body.fustrum.perceptionList.append(b.body)
            else:
                if not b.body.estMort:
                    agent.body.fustrum.perceptionList.append(b.body)

    for b in core.memory('items'):
        if agent.body.fustrum.inside(b):
            agent.body.fustrum.perceptionList.append(b)
    pass;

# def computeItemGestion(item):
#     for i in core.memory('items'):
#         if i.name == "Vegetal" and item.name == "Mineral":
#             print("Vegetal")
#             if i.body.position.distance_to(item.position) < item.body.size:
#                 i.level += 1
#                 print(i.level)

def computeDecision(agent):
    agent.update()

def applyDecision(agent):
    agent.body.update()

def run():
    core.cleanScreen()

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("items"):
        item.show()

    # for item in core.memory("agents"):
    #     computeItemGestion(item)

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnvironment()


core.main(setup, run)