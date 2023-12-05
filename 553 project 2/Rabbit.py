from Creature import Creature
import random

class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")

    def random_move(self, field_size):
        self.move(random.randint(0, field_size-1), random.randint(0, field_size-1))
