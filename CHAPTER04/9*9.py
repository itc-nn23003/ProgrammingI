def make_multfunc():
    def mult(x, y):
        return x * y

    for i in range(1, 10):
        for m in range(1, 10):
            result = mult(i, m)
            print(result, end=" ")
        print()


if __name__ == "__main__":
    make_multfunc()
