import random
import string

name = "I"


def f(name):
    while True:
        a = random.choice(string.ascii_lowercase)
        print(a)

        if a.upper() == name.upper():
            print("your name!")
            break


f(name)
