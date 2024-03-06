import random


def odds(o=25) -> bool:
    if o < 0:
        o = 0
    elif o > 100:
        o = 100
    num = random.randint(1, 100)
    return num <= o


for i in range(-10):
    print(odds())
