from sma_note.item import Item

#Représente la matière minérale libérée par un décomposeur
class Mineral(Item):
    def __init__(self, positionX=None, positionY=None):
        super().__init__(positionX, positionY)
        self.name = "mineral"
        self.color = (139, 69, 19) # marron
        self.size = 40