#Zhongyi Wang
from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.symbol} ({self.name}, {self.points})"
