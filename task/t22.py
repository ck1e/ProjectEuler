# What is the total of all the name scores in the file?

from string import ascii_uppercase


def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))


def main():
    with open('task/t22.txt') as file:
        names = file.read().split(',')
        names.sort()
    return sum(i * score(x) for i, x in enumerate(names, 1))
