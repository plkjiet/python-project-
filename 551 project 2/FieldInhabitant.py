#Zhongyi Wang
class FieldInhabitant:
    def __init__(self, symbol, x, y):
        self.symbol = symbol  # Symbol representing the inhabitant
        self.x = x            # X-coordinate
        self.y = y            # Y-coordinate

    def move(self, dx, dy):
        self.x += dx  # Move in x-direction
        self.y += dy  # Move in y-direction
