# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def main(start_number: int = 1, end_number: int = 100):
    difference = 0
    for i in range(start_number, end_number + 1):
        for j in range(i + 1, end_number + 1):
            difference += 2 * i * j
    return difference
