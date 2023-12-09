#Zhongyi Wang
import csv
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
import random

class GameEngine:
    def __init__(self):
        self.garden = []  # Represents the game field
        self.captain = None  # Captain of the game
        self.rabbits = []  # List of rabbits
        self.veggies = []  # List of vegetables

    def load_game_config(self, filepath):
        # Load game configuration from a CSV file
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Field Size':
                    self.garden = [['.' for _ in range(int(row[2]))] for _ in range(int(row[1]))]
                else:
                    self.veggies.append(Veggie(row[0], int(row[2]), int(row[3]), int(row[4])))

        # Set initial position for Captain and Rabbits
        self.captain = Captain(0, 0)
        for _ in range(2):  # Assuming two rabbits for example
            self.rabbits.append(Rabbit(random.randint(0, len(self.garden) - 1), random.randint(0, len(self.garden[0]) - 1)))

    def run_game(self):
        print("Welcome to Captain Veggie game!")
        self.load_game_config("VeggieFile.csv")
        while not self.check_game_over():
            self.render_game()
            self.process_user_input()
            self.update_game_state()
        print(f"Game over! Your score is: {self.captain.score}")

    def process_user_input(self):
        # Process player's move command
        move = input("Enter move command (e.g. 'up', 'down', 'left', 'right'): ")
        # Boundary check for movement
        if move == "up" and self.captain.y > 0:
            self.captain.move(0, -1)
        elif move == "down" and self.captain.y < len(self.garden) - 1:
            self.captain.move(0, 1)
        elif move == "left" and self.captain.x > 0:
            self.captain.move(-1, 0)
        elif move == "right" and self.captain.x < len(self.garden[0]) - 1:
            self.captain.move(1, 0)

    def update_game_state(self):
        # Update game state for each turn
        for rabbit in self.rabbits:
            rabbit.move_randomly(len(self.garden), len(self.garden[0]), self.veggies)
        self.captain.harvest(self)

    def render_game(self):
        # Render the game field
        field = [['.' for _ in range(len(self.garden[0]))] for _ in range(len(self.garden))]
        for veggie in self.veggies:
            field[veggie.x][veggie.y] = veggie.symbol
        for rabbit in self.rabbits:
            field[rabbit.x][rabbit.y] = 'R'
        field[self.captain.x][self.captain.y] = 'V'
        for row in field:
            print(' '.join(row))
        print(f"Score: {self.captain.score}")

    def check_game_over(self):
        # Check if the game is over
        return len(self.veggies) == 0
