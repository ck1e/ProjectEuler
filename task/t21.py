# Evaluate the sum of all the amicable numbers under 10000


def main(number: int = 1000000):
    limit = number * 10
    ds = [1] * limit
    for i in range(2, int(limit ** 0.5)):
        for j in range(i + 1, limit // i):
            ds[i * j] += i + j

    an = []
    for i in range(2, limit):
        if ds[i] < i and ds[ds[i]] == i:
            an += [ds[i], i]

    return sum(a for a in an if a < number)
