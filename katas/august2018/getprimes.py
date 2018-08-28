'''
Created on 27 Aug 2018

Finds the first N primes

@author: igoroya
'''
from math import sqrt


def is_prime(candidate):
    if candidate < 2:
        return False
    if candidate == 2:
        return True
    if candidate % 2 == 0:
        return False

    i = 3
    while i < sqrt(candidate):
        if candidate % i == 0:
            return False
        i += 1
    return True


def explore_and_check_if_primes(first, n):
    primes = []
    k = 0
    i = first
    while k < n:
        if is_prime(i):
            primes.append(i)
            k += 1
        i += 1
    return primes


def print_first_primes(n):
    primes = explore_and_check_if_primes(2, n)
    print(primes)


if __name__ == '__main__':
    print_first_primes(10)
