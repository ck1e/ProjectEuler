# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143

import math


def main(n: int = 600851475143):
    r = math.ceil(math.sqrt(n))
    lst = []
    for i in range(3, r):
        if n % i == 0:
            if not main(i):
                lst.append(i)

    return lst
