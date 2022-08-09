# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


def get_of_primes(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main(number: int = 10001):
    quantity, num = 2, 3
    while quantity != number:
        num += 2
        if get_of_primes(num):
            quantity += 1
    return num
