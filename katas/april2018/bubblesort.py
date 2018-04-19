'''
Created on 18 Apr 2018

@author: igoroya
'''
from random import randint


def bubble_sort(values):
    entries = len(values)

    while (entries > 1):
        for i in range(0, entries - 1):
            if values[i] > values[i+1]:
                swap(values, i, i+1)
        entries = entries - 1
    return values


def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp
    return values


if __name__ == '__main__':
    values = [randint(1, 1000) for i in range(1, 11)]
    print(values)
    new_values = bubble_sort(values)
    print(new_values)
