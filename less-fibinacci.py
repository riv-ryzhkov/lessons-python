n = int(input('Input number for counting Fibonacci number : '))
print(0, end=' ')
if n:
    print(1, end=' ')
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
        print(b, end=' ')
    print()
    print(n, "-th Fibonacci number is <", b, '>', sep='')