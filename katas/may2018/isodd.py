'''
Created on 2 May 2018

@author: igoroya
'''


def is_odd(number):
    return False if number % 2 == 0 else True


if __name__ == '__main__':
    value = input('insert one integer number\n')
    number = int(value)

    # old style
    # print('number %s inserted, is it odd? %s ' % (value, is_odd(number)))

    # new style
    print('number {} inserted, is it odd? {}'.format(number, is_odd(number)))
