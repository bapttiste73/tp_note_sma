import random

from pygame import Vector2

from sma_note.body import Body


class Agent(object):

    def __init__(self, body):
        self.name = "Agent"
        self.color = (255, 255, 255)
        self.body = body
        self.uuid = random.randint(100000, 999999999)
        self.perceptionList = []
        self.proies = []
        self.predateurs = []
        self.amis = []

    def filtrePerception(self):
        proies = []
        predateurs = []
        amis = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Body) and i.estMort == False:
                if i.name in self.proiesNames:
                    proies.append(i)
                if i.name in self.predateursNames and i.dort == False: #Si le predateur est en train de dormir, il ne peut pas manger et on en a pas peur
                    predateurs.append(i)
                if i.name in self.amisNames:
                    amis.append(i)

        proies.sort(key=lambda x: x.dist, reverse=False)
        predateurs.sort(key=lambda x: x.dist, reverse=False)
        amis.sort(key=lambda x: x.dist, reverse=False)

        return proies, predateurs, amis


    def update(self):
        self.proies, self.predateurs, self.amis = self.filtrePerception()
        self.body.acceleration += (self.mangeur(self.proies) + self.survie(self.predateurs) + self.symbiose(self.amis))

    def mangeur(self, proies):
        target = Vector2()
        if proies:
            target = self.proies[0].position - self.body.position
        return target

    def survie(self, predateurs):
        target = Vector2()
        if predateurs:
            target = self.body.position - self.predateurs[0].position
        return target

    def symbiose(self, amis):
        target = Vector2()
        if amis:
            target = self.amis[0].position - self.body.position
        return target


    def show(self):
        self.body.show()
