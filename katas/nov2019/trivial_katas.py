'''
Created on 15 Nov 2019

@author: igoroya
'''


def is_even(number):
    remainder = number % 2
    if remainder == 0:
        return True
    elif remainder == 1:
        return False
    else:
        raise ValueError('function not defined for this data type')


if __name__ == '__main__':
    for number in range(1, 25):
        print("is number: " + str(number) + " even?")
        print(is_even(number))

    my_number = "I am text"
    print("is number: " + str(my_number) + " even?")
    print(is_even(my_number))

    my_number = 145.7
    print("is number: " + str(my_number) + " even?")
    print(is_even(my_number))
