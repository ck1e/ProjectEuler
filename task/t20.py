# Find the sum of the digits in the number 100!

import math


def main(number: int = 100):
    s = 0
    number = math.factorial(number)
    while number > 1:
        s += number % 10
        number = number // 10
    return s
