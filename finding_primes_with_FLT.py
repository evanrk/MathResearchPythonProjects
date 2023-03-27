import math

# finding twin primes
def is_prime(number):
    for divisor in range(2, math.ceil(math.sqrt(number))+1):
        if number % divisor == 0:
            return False
    return True