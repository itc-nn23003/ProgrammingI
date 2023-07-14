import random

numbers = ["0", "1", "2", "4", "5", "6", "7", "8", "9"]
sample4 = random.sample(numbers, k=4)
num4 = "".join(sample4)

val = "".join(random.sample(numbers, k=4))
while True:
    if val == num4:
        print(val, ":OK")
        break
    else:
        print(val, ":NG")
        val = "".join(random.sample(numbers, k=4))
