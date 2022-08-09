# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations


def main(length: str = '0123456789', limit: int = 1000000):
    return ''.join(list(permutations(length))[limit - 1])
