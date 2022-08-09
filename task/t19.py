# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)

from datetime import date
from collections import Counter


def main(start_year: int = 1901, end_year: int = 2000):
    counter = Counter()
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            day = date(year, month, 1)
            counter[day.weekday()] += 1
    return counter[6]
