# Find the sum of all the primes below two million.


def main(max_number: int = 2000000):
    primes_list = list(range(max_number + 1))
    primes_list[1] = 0
    for i in primes_list:
        if i > 1:
            for j in range(i + i, len(primes_list), i):
                primes_list[j] = 0
    return sum(primes_list)
