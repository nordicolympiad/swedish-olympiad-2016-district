import random
import string

def replace(x):
    rnd = random.randint(0, 9)
    if rnd <= 2:
        return '#'
    return x

f = open("data.ans", "r").read().strip()

f = ''.join(replace(x) for x in f)

f2 = open("data.in", "w+")
f2.write(f)
f2.close()
