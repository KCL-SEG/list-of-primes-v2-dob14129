"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"{number_of_primes} is less than 1.")

    count = number_of_primes - 1
    num = 3
    list = []
    list.append(2)

    while count > 0:
        stillPrime = True
        i = 2
        while i <= num - 1 and stillPrime == True:
            if (num / i) % 1 == 0:
                stillPrime = False
                num += 1
            i += 1
        if stillPrime == True:
            list.append(num)
            num += 1
            count -= 1

    return list
