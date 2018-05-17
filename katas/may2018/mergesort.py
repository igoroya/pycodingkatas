'''
Created on 16 May 2018

@author: igoroya
'''
from random import randint


def rec_merge_sort(values):
    if len(values) == 1:
        return values

    elif len(values) > 1:
        mid = len(values)//2
        a = rec_merge_sort(values[:mid])
        b = rec_merge_sort(values[mid:])
        return merge_ordered(a, b)

    else:
        raise ValueError()


def merge_ordered(a, b):
    i = 0
    j = 0

    merged = []

    while (i < len(a) and j < len(b)):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


def sort_two(values, a, b):
    if values[b] > values[a]:
        tmp = values[b]
        values[a] = values[b]
        values[b] = tmp


if __name__ == '__main__':
    rand_values = [randint(1, 500) for i in range(1, 50)]
    print(rand_values)
    sorted_array = rec_merge_sort(rand_values)
    print(sorted_array)
