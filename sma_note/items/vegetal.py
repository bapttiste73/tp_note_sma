from sma_note.item import Item


class Vegetal(Item):
    def __init__(self, positionX=None, positionY=None):
        super().__init__(positionX, positionY)
        self.name = "Vegetal"
        self.color = (0, 255, 0) # vert
        self.size = 5
        self.level = 1