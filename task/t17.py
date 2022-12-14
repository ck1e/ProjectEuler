# Find the sum of all the primes below two million.


def main(number: int = 1001):
    unites = ['one', 'two', 'three', 'four', 'five',
              'six', 'seven', 'eight', 'nine', 'ten',
              'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    dizaines = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    autre = ['hundred', 'thousand', 'and']
    result = 0
    for i in range(1, number):
        unite = i % 10
        dizaine = (i // 10) % 10
        centaine = (i // 100) % 10
        millier = (i // 1000) % 10
        if millier != 0:
            result += len(unites[0]) + len(autre[1])
        if i % 1000 != 0:
            if centaine != 0:
                result += len(unites[centaine - 1]) + len(autre[0])
                if i % 100 != 0:
                    result += len(autre[2])
            if i % 100 != 0:
                if dizaine < 2:
                    result += len(unites[i % 100 - 1])
                else:
                    result += len(dizaines[dizaine - 2])
                    if unite != 0:
                        result += len(unites[unite - 1])
    return result
