# What is the value of the first triangle number to have over five hundred divisors?
from functools import reduce


def divisors(n):
    expList = []
    ctr = 0
    divisor = 2
    while divisor <= n:
        while n % divisor == 0:
            n = n/divisor
            ctr += 1
        if ctr != 0:
            expList.append(ctr+1)
        divisor += 1
        ctr = 0
    return reduce(lambda n, y: n * y, expList, 1)


def main(n: int = 500):
    natural = 1
    triangular_num = 0

    while True:
        triangular_num += natural
        natural += 1
        if divisors(triangular_num) > n:
            break
    return triangular_num
