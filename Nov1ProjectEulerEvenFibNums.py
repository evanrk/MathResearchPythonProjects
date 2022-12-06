# two liner:
# def fib2(n): return n if n <= 1 else (fib2(n-1) + fib2(n-2))
# print(sum(filter(lambda x: x <= 4000000, [fib2(n) for n in range(2, 4000000)])))

fib_list = [1, 2]
while True:
    n_fib = fib_list[-2] + fib_list[-1]
    if n_fib > 4000000:
        break
    fib_list.append(n_fib)

print(sum(fib_list))