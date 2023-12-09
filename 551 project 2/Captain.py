#Zhongyi Wang
from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__('V', x, y)  # 'V' represents the Captain
        self.score = 0  # Score of the Captain

    def harvest(self, garden):
        # Harvest vegetables
        for veggie in garden.veggies:
            if veggie.x == self.x and veggie.y == self.y:
                self.score += veggie.points  # Add points
                garden.veggies.remove(veggie)  # Remove harvested vegetable
                break
