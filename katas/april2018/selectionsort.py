'''
Created on 19 Apr 2018

@author: igoroya
'''
from random import randint


def sort(values):

    position = 0
    size = len(values)

    while position < size - 1:
        minimum = values[position]
        position_minumum = position
        for i in range(position, size):
            if values[i] < minimum:
                minimum = values[i]
                position_minumum = i
        swap(values, position, position_minumum)
        position = position + 1

    return values


def swap(values, first, second):
    temp = values[first]
    values[first] = values[second]
    values[second] = temp


if __name__ == '__main__':
    my_values = [randint(1, 100) for i in range(1, 11)]

    print(my_values)
    values_sorted = sort(my_values)
    print(values_sorted)
