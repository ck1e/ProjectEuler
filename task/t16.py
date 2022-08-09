# What is the sum of the digits of the number 21000?


def main(number: int = 2, power: int = 1000000):
    return sum(map(int, str(pow(number, power))))
