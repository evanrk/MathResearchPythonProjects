# Evan Klein
# 11/27/2022
# finding num and sum of divisors
 
from math import floor
 
def checkPrime(num):
  for i in range(2, floor(num**0.5)+1): # checks for every number between 2 and the square root of the given number
    if not(num%i): # checks to see if the number given to the function is divisible by the current number in the for loop
      return False # if the given number is divisible by the current number checkPrime returns false, because the number is not prime
  return True # if it gets through all the numbers and none are divisible, the number given is a prime, and checkPrime returns true
 
def findPrimeFactors(num):
  if checkPrime(num): # uses the checkPrime function above
    return [num] # if the number given is a prime number, it can return only the number given, because it is its only prime number
  for i in range(2, floor(num**0.5)+1): # iterates over every number from 2 to the square root of the given number
    if not(num%i): # if the given number is divisible by the current number:
      return findPrimeFactors(i) + findPrimeFactors(num//i) # the function calls itself, because it knows that the factors of two numbers that are divisible by each other make up the factors of the original number

def findDivisors(num):
  divisors = []
  for i in range(1, floor(num**0.5)+1):
    if not num%i:
      divisors += [i, num//i]
  return set(divisors)
 
def countDivisors(num):
    primes = findPrimeFactors(num) # uses the above function to find the prime factors of the given number
    divisors = 1 # instantiates the divisors variable
    for prime in set(primes): # set() is a function that creates a Set object, where there are no duplicates of any value in the set, it uses this to iterate over every unique prime in the prime factors
        divisors *= primes.count(prime) + 1 # for every unique prime it multiplies the amount of times it appears in the list of prime factors, created earlier, which gives the power. This, plus 1 is then multiplied to the number of divisors
    return divisors # returns divisors
 
def sumDivisors(num):
    primes = findPrimeFactors(num) # same as the above function
    divisorsSum = 1 # instantiates the divisorsSum variable
    for prime in set(primes): # same as above function
        divisorsSum *= sum([prime**power for power in range(primes.count(prime)+1)]) # takes the sum of the prime for every power from 0 to the power of the prime
    return divisorsSum # returns divisorsSum
 
def outputFunc(num):
    if checkPrime(num): # uses the checkPrime function
        return f"{num} is prime!\nthe divisors are {list(findDivisors(num))}\nthe prime factorization is {findPrimeFactors(num)}" # returns "num is prime", the divisors, and the prime factorization if the number is prime
    else:
        return f"{num}:\nthe prime factorization of {num} is {findPrimeFactors(num)}\nthe divisors are {list(findDivisors(num))}\nthe number of divisors of {num} is {countDivisors(num)}\nthe sum of the divisors of {num} is {sumDivisors(num)}" # returns the divisors, the prime factorization, the number of divisors, and the sum of the divisors if the number is not prime


# prime number
print(outputFunc(17)) # should return prime

# composite number
print(outputFunc(1400)) # should return 24 and 3720

# perfect square
print(outputFunc(25**2))