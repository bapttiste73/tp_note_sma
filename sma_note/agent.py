import random

class Agent(object):

    def __init__(self, body):
        self.name = "Agent"
        self.color = (255, 255, 255)
        self.body = body
        self.uuid = random.randint(100000, 999999999)
        self.perceptionList = []
        self.proies = []
        self.predateurs = []

    def filtrePerception(self):
        proies = []
        predateurs = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if i.name in self.proiesName:
                proies.append(i)
            if i.name in self.predateursNames:
                predateurs.append(i)

        proies.sort(key=lambda x: x.dist, reverse=False)
        predateurs.sort(key=lambda x: x.dist, reverse=False)

        return proies, predateurs



    def update(self):
        self.proies, self.predateurs = self.filtrePerception()

        if self.predateurs:
            target = self.predateurs[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acceleration += target

        if self.proies:
            target = self.body.position - self.proies[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.body.mass))
            self.body.acceleration += target


    def show(self):
        self.body.show()
