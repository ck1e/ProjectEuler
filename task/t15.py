# How many such routes are there through a 20×20 grid?

import math


def main(x: int = 20, y: int = 20):
    return math.factorial(x + y) / (math.factorial(x) * math.factorial(y))
