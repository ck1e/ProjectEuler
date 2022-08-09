# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


def main(start_number: int = 100, end_number: int = 1000):
    palindromics = []
    for i in range(end_number - 1, start_number - 1, -1):
        for j in range(end_number - 1, start_number - 1, -1):
            if str(i * j) == str(j * i)[::-1]:
                palindromics.append(i * j)
    return max(palindromics)
