#Zhongyi Wang
from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, symbol, points, x, y):
        super().__init__(symbol, x, y)  # Initialize the base class
        self.points = points  # Points for the vegetable
