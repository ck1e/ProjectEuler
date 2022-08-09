# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main(max_sum: int = 1000):
    for n in range(1, max_sum + 1):
        for m in range(n + 1, max_sum + 1):
            if (m - n) % 2 == 0:
                continue
            if ((m ** 2 - n ** 2) + (2 * m * n) + (m ** 2 + n ** 2)) == max_sum:
                return (m ** 2 - n ** 2) * (2 * m * n) * (m ** 2 + n ** 2)
