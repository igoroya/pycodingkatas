'''
Created on 19 Apr 2018

@author: igoroya
'''
from random import randint, random


def sort(values):
    """
    Implements a selection sort for any number type
    """
    size = len(values)

    for sorted_limit_index in range(0, size):
        value_being_sorted = values[sorted_limit_index]
        for i in range(0, sorted_limit_index):
            if value_being_sorted < values[i]:
                shift_one_up_from_index(values, i, sorted_limit_index)
                values[i] = value_being_sorted
                break
    return values


def shift_one_up_from_index(values, first_index, last_index):
    """
    Shift values one position up starting from first_index,
    filling up to last_index
    """
    for i in range(last_index, first_index, -1):
        values[i] = values[i-1]


if __name__ == '__main__':
    my_values = [randint(1, 1000) for i in range(1, 11)]
    print(my_values)
    new_values = sort(my_values)
    print(new_values)

    my_values = [1000*random() for i in range(1, 11)]
    print(my_values)
    new_values = sort(my_values)
    print(new_values)
