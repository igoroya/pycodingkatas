'''
Created on 11 May 2018

Module to experiment with comprehension-s and generators

@author: igoroya
'''
import string


def get_even_numbers(entries):
    numbers = [i for i in range(1, 2*entries+1) if i % 2 == 0]
    return numbers


def create_powers_of_two(entries):
    numbers = [2**i for i in range(1, entries)]
    return numbers


def get_letters():
    letters = [s for s in string.ascii_lowercase]
    return letters


if __name__ == '__main__':
    number_of_evens = 20
    print(get_even_numbers(number_of_evens))
    print(create_powers_of_two(number_of_evens))
    print(get_letters())
