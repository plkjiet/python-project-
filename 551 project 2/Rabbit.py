#Zhongyi Wang
from Creature import Creature
import random

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__('R', x, y)  # 'R' represents the Rabbit

    def move_randomly(self, max_x, max_y, veggies):
        # Move randomly and eat vegetables if present
        new_x, new_y = self.x, self.y
        while new_x == self.x and new_y == self.y:
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])
            new_x = min(max(0, self.x + dx), max_x - 1)
            new_y = min(max(0, self.y + dy), max_y - 1)

        self.eat_veggie(new_x, new_y, veggies)
        self.x, self.y = new_x, new_y

    def eat_veggie(self, x, y, veggies):
        # Eat vegetable if present at the new position
        for veggie in veggies:
            if veggie.x == x and veggie.y == y:
                veggies.remove(veggie)
                break
