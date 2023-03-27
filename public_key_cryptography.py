import math
import random

SIZE = 100

def is_prime(number):
	for divisor in range(2, math.ceil(math.sqrt(number))+1):
		if number % divisor == 0:
			return False
	return True

def gcd(a, b): return (a+b if a+b != 1 else False) if not a or not b else gcd(b, a%b)

primes = []

for num in range(2, SIZE):
	if is_prime(num):
		primes.append(num)


p = primes.pop(random.randint(0, len(primes)-1))
q = primes.pop(random.randint(0, len(primes)-1))

p = 3
q = 7

print(f"p: {p} q: {q}")

n = p*q
phi_n = (p-1)*(q-1)

# relatively prime to phi_n
e = 3

while gcd(e, phi_n):
	e += 1

k = 1
d = (k * phi_n + 1) / e

while int(d) != d:
	k += 1
	d = (k * phi_n + 1) / e

print(f"k: {k}")
print(f"e: {e}")
print(f"d: {d}")

message = 12

encrypted = message ** e % n
print(encrypted)
decrypted = math.fmod(encrypted ** d, n)
print(decrypted)