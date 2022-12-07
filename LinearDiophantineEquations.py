# equation = input("Enter your linear diophantine equation in the input ax + by = c  ")

def gcd(a, b, iter=0): return ((a+b) if a+b != 1 else 1) if not a or not b else gcd(b, a%b, iter+1) # function from before that finds the gcd of two numbers
# def reverseEuclidAlg(a, b, iter=0):

print(gcd(252, 198))

fa;sdfhasdkjlfsbl

# def diophantineSolver(a, b, c):
#     gcd = gcd(a, b)
