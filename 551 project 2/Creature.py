#Zhongyi Wang
from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, symbol, x, y):
        super().__init__(symbol, x, y)  # Initialize the base class
