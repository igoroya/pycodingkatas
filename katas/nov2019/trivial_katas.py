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


def test_is_even():
    for number in range(1, 25):
        print("is number: " + str(number) + " even?")
        print(is_even(number))

    my_number = "I am text"
    print("is number: " + str(my_number) + " even?")
    print(is_even(my_number))

    # my_number = 145.7
    # print("is number: " + str(my_number) + " even?")
    # print(is_even(my_number))


'''
Find the first N primes
'''
def print_primes(ammount):

    found_primes = [1, 2]
    candidate = 3

    while (len(found_primes) < ammount):
        #print(candidate)
        is_prime = True
        for prime in found_primes[1:]:
            if candidate % prime == 0:
                #print('not prime')
                is_prime = False
                break
        if is_prime:
            #print('prime')
            found_primes.append(candidate)
        candidate += 2

    print(found_primes)


def test_print_primes():
    print_primes(100)


if __name__ == '__main__':
    test_print_primes()
