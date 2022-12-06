def gcd(a, b, iter=0): return (a+b if a+b != 1 else "relatively prime!", f"iterations: {iter}") if not a or not b else gcd(b, a%b, iter+1) 
# takes the first two values, if either of the values is zero, it returns the sum of the values, which is the output, if both of them are not, the function passes b 
# and the remainder of a divided by b into itself, repeating the process until one of them is zero. In the end, the function returns the final common denominator and amount of iterations; if the common denominator equals 1, the function returns relatively prime with the iterations instead of 1

# max = ([0, 0], 0, 0)
# for a in range(1, 100000):
#     for b in range(1, 100000):
#         num = gcd(a, b)
#         if num[1] > max[2]:
#             max = ([a, b], num[0], num[1])
# print("Greatest Common Denominator:")
# print("40 and 30: "+ "".join([(("\nGreatest Common Denominator: "+str(output)+"\n") * int(not index)) + (("Iterations: "+str(output)) * int(index)) for index, output in enumerate(gcd(40, 30))]))
# 10001 and 100083: 
#     {gcd(100083, 10001)}
# 25578 and 3852: 
#     {gcd(25578, 3852)}""")

print("Starting 1000083, 10001:", gcd(100083, 10001))
print("Starting 25578, 3852:", gcd(25578, 3852))
print("Starting 40, 30:", gcd(40, 30))
print("Starting 100, 50:", gcd(100, 50))
print("Starting 5000, 500:",gcd(5000, 500))
print("Starting 180347209128347, 121093", gcd(180347209128347, 121093))