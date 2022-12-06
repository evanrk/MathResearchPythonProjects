limit = 11
from functools import reduce
# for a in range(2, limit):
#     for n in range(0, limit): 
#         recursive = int(sum([a**i for i in range(0, n+1)]))
#         explicit = int((a**(n+1) - 1)//(a-1))
#         print(f"{recursive} == {explicit}: {recursive == explicit}")
#         if recursive != explicit:
#             print("not equal")
#             quit()
# print("equal!")

print("Equal!") if reduce(lambda first, second: first and second, reduce(lambda first, second: first and second, [([(int(sum([a**i for i in range(0, n+1)]))) == int((a**(n+1) - 1)/(a-1)) for n in range(0, limit)]) for a in range(2, limit)])) else print("Not equal")