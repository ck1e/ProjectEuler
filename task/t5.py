# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def gcd(one_number, two_number):
    while two_number > 0:
        one_number, two_number = two_number, one_number % two_number
    return one_number


def lcm(one_number, two_number):
    return one_number * two_number // gcd(one_number, two_number)


def main(one_number: int = 1, two_number: int = 20):
    num_list = []

    d = 1
    for i in range(one_number + 1, two_number + 1):
        d = lcm(d, i)
        num_list.append(d)
    return max(num_list)
