# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math


def getDivisors(num):
    if num == 1:
        return False
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while divisor < n:
        if num % divisor == 0:
            total += divisor
            total += num // divisor
        divisor += 1
    if n ** 2 == num:
        total += n
    if total > num:
        return True
    else:
        return False


def main(limit: int = 28124):
    abundentNums = [x for x in range(1, limit) if getDivisors(x)]
    total = 0
    sums = [0] * limit

    for x in range(0, len(abundentNums)):
        for y in range(x, len(abundentNums)):
            if abundentNums[x] + abundentNums[y] <= limit - 1:
                if sums[abundentNums[x] + abundentNums[y]] == 0:
                    sums[abundentNums[x] + abundentNums[y]] = abundentNums[x] + abundentNums[y]

    for x in range(1, len(sums)):
        if sums[x] == 0:
            total += x

    return total
