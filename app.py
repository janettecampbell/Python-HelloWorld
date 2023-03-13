# Generating Random Numbers

import random


class Dice:
    def roll(self):
        random_x = random.randint(1, 6)
        random_y = random.randint(1, 6)
        return random_x, random_y


roll1 = Dice()

print(roll1.roll())