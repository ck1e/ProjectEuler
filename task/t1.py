# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


def main(max_number: int = 1000, one_divide: int = 3, two_divide: int = 5) -> int:
    return sum([x for x in range(1, max_number) if x % one_divide == 0 or x % two_divide == 0])
