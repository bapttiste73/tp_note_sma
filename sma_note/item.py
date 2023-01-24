import random

from pygame import Vector2

import core

class Item(object):

    def __init__(self, positionX=None, positionY=None):
        if positionX and positionY:
            self.position = Vector2(positionX, positionY)
        else:
            self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))


    def show(self):
        core.Draw.circle(self.color, self.position, self.size)