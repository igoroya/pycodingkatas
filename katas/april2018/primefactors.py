'''
Simple prime factors determination kata

Created on 3 Apr 2018

@author: igoroya
'''

def find_prime_factors(number):
    
    factors = []
    current_number = number;

    res = find_a_divisor(current_number)

    while res is not None:
        current_number = current_number // res
        factors.append(res)
        res = find_a_divisor(current_number)
    
    return factors
        
def find_a_divisor(my_number):
    
    if my_number <= 1:
        return None

    for i in range(2, my_number + 1):
        if is_divisible(i, my_number):
            return i
    
    return None
             
            
def is_divisible(my_candidate, my_number):
    return True if my_number % my_candidate is 0 else False
    

        
if __name__ == '__main__':
    print("Determine prime factors")
    factors = find_prime_factors(39)
    print(factors)