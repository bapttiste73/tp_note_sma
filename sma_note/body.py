import datetime
import random

from pygame import Vector2

import core
from fustrum import Fustrum

class Body(object):

    def __init__(self):
        self.dort = False
        self.dateNaissance = datetime.datetime.now()
        self.esperanceVie = self.dateNaissance + datetime.timedelta(days=365)
        self.estMort = False
        self.vientDeManger = False


        self.vitesse = Vector2(random.randint(-5, 5), random.randint(-5, 5))
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.acceleration = Vector2()
        self.fustrum = Fustrum(20, self)
        self.mass = 10
        self.maxForce = 0.1
        self.perception = 100

    def update(self):
        if self.estMort:
            self.dort = False
            return

        if not self.dort:
            self.move()

        if self.vientDeManger:
            self.niveauFaim = 0
            self.vientDeManger = False

        #Trop vieux
        if datetime.datetime.now() > self.esperanceVie:
            print("Mort d'age")
            self.estMort = True
            return

        #Fatigue
        if self.dort:
            if self.niveauFatigue > 0:
                self.niveauFatigue -= 5
            else:
                self.dort = False

            if self.niveauFaim > 0:
                self.niveauFaim -= 0.25
        else:
            self.niveauFatigue += 1

        if self.niveauFatigue >= self.maxFatigue:
            self.dort = True

        if self.niveauFatigue <= 0:
            self.dort = False

        #Faim
        if self.dort:
            if self.niveauFaim > 0:
                self.niveauFaim -= 1
        else:
            self.niveauFaim += 0.5

        if self.niveauFaim >= self.maxFaim:
            self.estMort = True
            return

        #Reproduction
        if self.niveauFaim < (self.maxFaim * 0.1) and self.niveauFatigue < (self.maxFatigue * 0.1):
            self.niveauReproduction += 10*random.randint(1,5)


        if self.niveauReproduction >= self.maxReproduction and not self.dort:
            print(self.niveauReproduction)
            self.reproduction()
            self.niveauReproduction = 0

    def show(self):

        # if self.estMort is False:
        #     core.Draw.text(self.color, str(self.niveauFatigue) + " " + str (self.niveauFaim), Vector2(self.position.x - 10, self.position.y - 30), taille=15)

        if self.dort:
            core.Draw.text(self.color, "Zzz", Vector2(self.position.x - 10, self.position.y - 30), taille=15)
        if self.estMort:
            core.Draw.text(self.color, "x", Vector2(self.position.x - 5, self.position.y - 30), taille=15)
        core.Draw.circle(self.color, self.position, self.mass)

    def move(self):
        if self.acceleration.length() > self.accelMax:
            self.acceleration.scale_to_length(self.accelMax)

        self.vitesse += self.acceleration
        if self.vitesse.length() > self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)

        self.position += self.vitesse
        self.acceleration = Vector2(0, 0)
        self.edge()

    def edge(self):
        if self.position.x <= self.mass:
            self.vitesse.x *= -1
            self.position.x = self.mass
        if self.position.x + self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
            self.position.x = core.WINDOW_SIZE[0] - self.mass
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
            self.position.y = self.mass
        if self.position.y + self.mass >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1
            self.position.y = core.WINDOW_SIZE[1] - self.mass