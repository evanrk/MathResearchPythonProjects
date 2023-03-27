import math


def is_prime(num):
    if num == 2:
        return True
    for divisor in range(2, math.ceil(math.sqrt(num))+1):
        if num % divisor == 0:
            return False
    return True

def find_prime_factors(num):
    if is_prime(num): 
        return [num] 
    for i in range(2, math.floor(num**0.5)+1):
        if num%i == 0:
            return find_prime_factors(i) + find_prime_factors(num//i)

def find_divisors(num):
    divisors = []
    for i in range(2, math.floor(num**0.5)+1):
        if not num%i:
            divisors += [i, num//i]
    divisors = list(set(divisors))
    divisors.sort()
    return divisors


STOP = 10000

f_d = input("f_d = ")

for num in range(2, STOP+1):
    if is_prime(num) and is_prime(num+2):
        if f_d == "f":
            print(f"{num}, {num+2}: {find_prime_factors(num+1)}")
        elif f_d == "d":
            print(f"{num}, {num+2}: {find_divisors(num+1)}")
            