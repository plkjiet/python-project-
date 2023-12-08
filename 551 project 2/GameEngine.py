#Zhongyi Wang
from Captain import Captain
from Rabbit import Rabbit
from Veggie import Veggie
import random
class GameEngine:
    def __init__(self):
        self.field_size = 10
        self.field = [[None for _ in range(self.field_size)] for _ in range(self.field_size)]
        self.captain = Captain(0, 0)
        self.rabbits = [Rabbit(9, 9)]
        self.veggies = [Veggie("Carrot", "C", 5), Veggie("Lettuce", "L", 10)]
        self.initGame()

    def initGame(self):
        # Initialize veggies at random positions
        for veggie in self.veggies:
            x, y = random.randint(0, self.field_size - 1), random.randint(0, self.field_size - 1)
            while self.field[x][y] is not None:
                x, y = random.randint(0, self.field_size - 1), random.randint(0, self.field_size - 1)
            self.field[x][y] = veggie

        # Place Captain and Rabbit
        self.field[self.captain.x][self.captain.y] = self.captain
        for rabbit in self.rabbits:
            self.field[rabbit.x][rabbit.y] = rabbit

    def printField(self):
        for row in self.field:
            print(' '.join([inhabitant.get_symbol() if inhabitant else '.' for inhabitant in row]))

    def moveCaptain(self, direction):
        # Remove captain from current position
        self.field[self.captain.x][self.captain.y] = None

        # Update captain's position based on direction
        if direction == "up" and self.captain.x > 0:
            self.captain.x -= 1
        elif direction == "down" and self.captain.x < self.field_size - 1:
            self.captain.x += 1
        elif direction == "left" and self.captain.y > 0:
            self.captain.y -= 1
        elif direction == "right" and self.captain.y < self.field_size - 1:
            self.captain.y += 1

        # Collect veggie if present
        current_pos = self.field[self.captain.x][self.captain.y]
        if isinstance(current_pos, Veggie):
            self.captain.addVeggie(current_pos.points)
            self.veggies.remove(current_pos)

        # Place captain at new position
        self.field[self.captain.x][self.captain.y] = self.captain

    def moveRabbits(self):
        for rabbit in self.rabbits:
            # Remove rabbit from current position
            self.field[rabbit.x][rabbit.y] = None

            # Move rabbit to new position
            rabbit.random_move(self.field_size)
            current_pos = self.field[rabbit.x][rabbit.y]

            # If rabbit lands on veggie, remove veggie
            if isinstance(current_pos, Veggie):
                self.veggies.remove(current_pos)

            # Place rabbit at new position
            self.field[rabbit.x][rabbit.y] = rabbit

    def checkGameOver(self):
        return len(self.veggies) == 0

    def start(self):
        while not self.checkGameOver():
            self.printField()
            direction = input("Move Captain (up, down, left, right): ")
            self.moveCaptain(direction)
            self.moveRabbits()

            if self.checkGameOver():
                print("Game Over. Score:", self.captain.veggies_collected)
                break
