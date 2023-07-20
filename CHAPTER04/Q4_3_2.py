def func_square(*args):
    result = []
    for n in args:
        result.append(n * n)
    return result


numbers = [1, 2, 3, 4]
print(func_square(*numbers))

numbers = list(range(100))
print(func_square(*numbers))
