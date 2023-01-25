import json
import time

import pygame
from pygame import Vector2

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

import matplotlib.pyplot as plt
import threading

def setup():
    print("Setup START---------")

    load("scenario.json")

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("items", [])

    for i in range(core.memory('scenario')["SuperPredateur"]["nb"]):
        core.memory('agents').append(SuperPredateur(bodySuperPredateur()))

    for i in range(core.memory('scenario')["Carnivore"]["nb"]):
        core.memory('agents').append(Carnivore(bodyCarnivore()))

    for i in range(core.memory('scenario')["Herbivore"]["nb"]):
        core.memory('agents').append(Herbivore(bodyHerbivore()))

    for i in range(core.memory('scenario')["Decomposeur"]["nb"]):
        core.memory('agents').append(Decomposeur(bodyDecomposeur()))

    for i in range(core.memory('scenario')["Vegetal"]["nb"]):
        core.memory('items').append(Vegetal())

    plotThread = threading.Thread(target=printPopulationGraph, args=())
    plotThread.start()

    print("Setup END-----------")

def updateEnvironment():
    for a in core.memory('agents'):
        for b in core.memory('agents'):
            if a.uuid != b.uuid:
                if a.body.position.distance_to(b.body.position) < 10:
                    if a.name != "Decomposeur" and a.name in b.predateursNames:
                        a.body.vientDeManger = True
                        b.body.estMort = True
                        print(a.name + " a mangé " + b.name)
                    if a.name == "Decomposeur" and b.body.estMort:
                        a.body.vientDeManger = True
                        core.memory('items').append(Vegetal(b.body.position.x, b.body.position.y))
                        core.memory('agents').remove(b)


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

def computeItemGestion(item):
    if item.name == "Vegetal":
        item.update()
        for a in core.memory('agents'):
            if a.name == "Herbivore" and a.body.position.distance_to(item.position) < item.size:
                if item in core.memory('items'):
                    core.memory('items').remove(item)
                    a.body.vientDeManger = True


def computeDecision(agent):
    agent.update()

def applyDecision(agent):
    agent.body.update()

def load(path):
    f = open(path)
    data = json.load(f)
    core.memory("scenario", data)
    f.close()

def getBestAgent():
    best = core.memory('agents')[0]
    for a in core.memory('agents'):
        if not a.body.estMort and a.body.geneticScore > best.body.geneticScore:
            best = a
    return best

def getNbIndividus():
    nbHerbivore = 0
    nbCarnivore = 0
    nbDecomposeur = 0
    nbSuperPredateur = 0
    for a in core.memory('agents'):
        if not a.body.estMort:
            if a.name == "Herbivore":
                nbHerbivore += 1
            if a.name == "Carnivore":
                nbCarnivore += 1
            if a.name == "Decomposeur":
                nbDecomposeur += 1
            if a.name == "SuperPredateur":
                nbSuperPredateur += 1

    return nbSuperPredateur, nbCarnivore, nbHerbivore, nbDecomposeur

#Affiche le pourcentage de chaque espèce dans la console
def printPopulationPourcentage(nbSuperPredateur, nbCarnivore, nbHerbivore, nbDecomposeur):
    print("Pourcentage de SuperPredateur : " + str(round(nbSuperPredateur / len(core.memory('agents')) * 100)) + "%")
    print("Pourcentage de Carnivore : " + str(round(nbCarnivore / len(core.memory('agents')) * 100)) + "%")
    print("Pourcentage de Herbivore : " + str(round(nbHerbivore / len(core.memory('agents')) * 100)) + "%")
    print("Pourcentage de Decomposeur : " + str(round(nbDecomposeur / len(core.memory('agents')) * 100)) + "%")

#Afficher un graphique en temps réel des populations
history_time = []
glob_data = {"Herbivore": [], "Carnivore": [], "SuperPredateur": [], "Vegetal": [], "Decomposeur": []}

def printPopulationGraph():
    while True:
        data = {'Herbivore': 0, 'Carnivore': 0, 'SuperPredateur': 0, 'Vegetal': 0, 'Decomposeur': 0}
        for agent in core.memory("agents"):
            if not agent.body.estMort:
                data[agent.body.name] += 1

        for item in core.memory("items"):
            data["Vegetal"] += 1

        plt.cla()
        history_time.append(pygame.time.get_ticks() / 1000)

        for key in glob_data.keys():
            glob_data[key].append(data[key])
            switcher = {
                "SuperPredateur": 'red',
                "Carnivore": 'yellow',
                "Herbivore": 'cyan',
                "Decomposeur": 'grey',
                "Vegetal": 'green',
            }
            color = switcher.get(key, "Agent inconnu")
            plt.plot(history_time, glob_data[key], color, label=key)

        plt.xlabel('Temps (s)')
        plt.ylabel('Nombre de cas')
        plt.legend(loc="center right")
        plt.title("Evolution des différents individus")
        plt.ion()
        plt.draw()
        plt.show()
        plt.pause(0.001)


def run():
    core.cleanScreen()

    best = getBestAgent()

    # Display
    for agent in core.memory("agents"):
        if agent == best:
            core.Draw.text(agent.body.color, "Best Agent" + str(agent.body.geneticScore), Vector2(agent.body.position.x - 20,  agent.body.position.y + 10), taille=15)

        agent.show()

    for item in core.memory("items"):
        item.show()

    for item in core.memory("items"):
        computeItemGestion(item)

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    #Console display
    print("L'agent avec la meilleur génétique est : " + getBestAgent().name + " avec un score de : " + str(getBestAgent().body.geneticScore))
    nbSuperPredateur, nbCarnivore, nbHerbivore, nbDecomposeur = getNbIndividus()
    printPopulationPourcentage(nbSuperPredateur, nbCarnivore, nbHerbivore, nbDecomposeur)
    print("--------------------")

    updateEnvironment()


core.main(setup, run)