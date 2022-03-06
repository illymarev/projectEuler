import math


def _is_prime(n):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0

    i = 3
    range = int(math.sqrt(n)) + 1
    while (i < range):
        if (n % i == 0):
            return 0
        i += 1
    return 1


start = 3
primes = 0
while primes < 10000:
    if _is_prime(start):
        primes += 1
    start += 2
print(start - 2)
