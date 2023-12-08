#Zhongyi Wang
from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self.veggies_collected = 0

    def addVeggie(self, points):
        self.veggies_collected += points
