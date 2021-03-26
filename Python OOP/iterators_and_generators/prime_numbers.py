from math import sqrt


def get_primes(integers):
    def is_prime(number):
        for x in range(2, int(sqrt(number)) + 1):
            if number % x == 0:
                return False
        return True

    for number in integers:
        if number > 1 and is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))