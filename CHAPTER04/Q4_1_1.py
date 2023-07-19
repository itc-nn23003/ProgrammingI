def fib(n):
    a, b = 0, 1
    print(a)
    print(b)
    while a < n:
        c = a + b
        print(c)
        a = b
        b = c


fib(15)


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end="")
        a, b = b, a + b


fib(15)
