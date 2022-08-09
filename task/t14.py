# Which starting number, under one million, produces the longest chain?


def main(number: int = 1000000):
    search_elem = 0
    len_Collatz = 0
    sequence_length = {1: 0}

    def Collatz_sequence_length(elem):
        if elem in sequence_length:
            return sequence_length[elem]
        if elem%2 == 0:
            length = Collatz_sequence_length(elem//2)
        else:
            length = Collatz_sequence_length(3*elem + 1)
        length += 1
        sequence_length[elem] = length
        return length

    for i in range(1, number):
        length = Collatz_sequence_length(i)
        if length > len_Collatz:
            search_elem = i
            len_Collatz = length
    return search_elem
