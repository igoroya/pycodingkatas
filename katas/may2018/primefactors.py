'''
Created on 10 May 2018

@author: igoroya
'''


def get_prime_factors(number):

    if number < 2:
        return None

    factors = []
    remainder = number

    while (remainder >= 2):
        for possible_divisor in range(2, remainder + 1):
            if remainder % possible_divisor == 0:
                factors.append(possible_divisor)
                remainder = remainder // possible_divisor
                break
    return factors


if __name__ == '__main__':
    input_number = int(input('Insert a possitive integer\n'))
    factors = get_prime_factors(input_number)
    print('The prime factors of {} are {}'.format(input_number, factors))
