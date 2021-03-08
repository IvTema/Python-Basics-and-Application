'''https://stepik.org/lesson/24464/step/5?auth=registration&unit=6769'''
from math import sqrt
import itertools


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def primes():
    n = 2
    while True:
        if is_prime(n) is True:
            yield n
        n += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))

