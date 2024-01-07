
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# fib(4)-> fib(3)=2 -> fib(2)=1
#          fib(3) -> fib(2)=1 -> fib(1)=1+0
#                    fib(2) -> fib(1)=1+0

#
#
# for i in range(12):
#     print(fib(i), end=' ')
#
#