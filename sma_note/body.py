import datetime
import random

from pygame import Vector2

import core
from fustrum import Fustrum

class Body(object):

    def __init__(self):
        self.vitesse = Vector2(random.randint(-5, 5), random.randint(-5, 5))
        self.vitesseMax = 1
        self.accelMax = 2

        self.niveauFatigue = 0
        self.maxFatigue = 1000
        self.dort = False

        self.niveauFaim = 0
        self.maxFaim = 1000

        self.niveauReproduction = 0
        self.maxReproduction = 1000

        self.dateNaissance = datetime.datetime.now()
        self.estMort = False

        self.vientDeManger = False

        self.color = (255, 255, 0)

        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.acceleration = Vector2()
        self.fustrum = Fustrum(300, self)
        self.mass = 10
        self.maxvitesse = 2
        self.maxForce = 0.1
        self.perception = 100

    def update(self):
        if self.estMort:
            return

        if(self.dort == False):
            self.move()

        if self.vientDeManger == True:
            self.niveauFaim = 0
            self.vientDeManger = False


        #Trop vieux
        # if datetime.datetime.now() > self.esperanceVie:
        #     print("Mort d'age")
        #     self.estMort = True
        #     self.color = (50, 50, 50)
        #     return

        #Fatigue
        if self.dort:
            if self.niveauFatigue > 0:
                self.niveauFatigue -=1
            else:
                self.dort = False

            if self.niveauFaim > 0:
                self.niveauFaim -=0.25
        else:
            self.niveauFatigue += 1

        if self.niveauFatigue >= self.maxFatigue:
            self.dort = True
        if self.niveauFatigue <= 0:
            self.dort = False

        #Faim
        if(self.dort == True):
            if self.niveauFaim > 0:
                self.niveauFaim -= 1
        else:
            self.niveauFaim += 0.5

        if self.niveauFaim >= self.maxFaim:
            print("Mort de faim")
            self.estMort = True
            self.color = (50, 50, 50)
            return

        #Reproduction
        if self.niveauFaim < self.maxFaim / 2 and self.niveauFatigue < self.niveauFatigue /2:
            self.niveauReproduction += 50
        if(self.niveauReproduction >= self.maxReproduction):
            self.dedouble()


    def show(self):
        # if self.estMort is False:
            # core.Draw.text(self.color, str(self.niveauFatigue) + " " + str (self.niveauFaim), Vector2(self.position.x - 10, self.position.y - 30), taille=15)
        core.Draw.circle(self.color, self.position, self.mass)

    def update(self):
        if self.acceleration.length() > self.accelMax:
            self.acceleration.scale_to_length(self.accelMax)

        self.vitesse += self.acceleration
        if self.vitesse.length() > self.vitesseMax:
            self.vitesse.scale_to_length(self.vitesseMax)
        self.acceleration = Vector2(0, 0)
        self.position += self.vitesse
        self.edge()

    def repultion(self, obstacle):
        obstacleVect = Vector2(obstacle[0], obstacle[1])
        if obstacleVect.distance_to(self.position) < self.perception * 2:
            self.acceleration = self.position - obstacleVect

    def attraction(self, obstacle):
        obstacleVect = Vector2(obstacle[0], obstacle[1])
        if obstacleVect.distance_to(self.position) < self.perception * 2:
            self.acceleration = obstacleVect - self.position

    def move(self):
        if self.acceleration.length() > self.accelMax:
            self.acceleration.scale_to_length(self.accelMax)

        self.vitesse += self.acceleration
        if self.vitesse.length() > self.maxvitesse:
            self.vitesse.scale_to_length(self.maxvitesse)

        self.position += self.vitesse
        self.acceleration = Vector2(0, 0)
        self.edge()

    def edge(self):
        if self.position.x <= self.mass:
            self.vitesse.x *= -1
        if self.position.x + self.mass >= core.WINDOW_SIZE[0]:
            self.vitesse.x *= -1
        if self.position.y <= self.mass:
            self.vitesse.y *= -1
        if self.position.y + self.mass >= core.WINDOW_SIZE[1]:
            self.vitesse.y *= -1