import random
import re
import string
import sys

def fish(txt):
    txt = re.sub("[A-Z][a-z]+", "Fisk", txt)
    txt = re.sub(" [a-z]+", " fisk", txt)
    return txt

def az(txt):
    ntxt = []
    for i in txt:
        if txt in string.ascii_lowercase:
            ntxt.append(i)
    return ''.join(ntxt)

def encode(txt, key):
    ntxt = []
    for i, el in enumerate(txt):
        ntxt.append(ord(el) ^ key[i % len(key)])
    return ntxt

def hexa(txt):
    ans = ""
    for i in txt:
        i = hex(i)[2:]
        if len(i) < 2: i = "0" + i
        ans += i
    return ans

random.seed(int(sys.argv[1]))

path = "texts/" + sys.argv[2]

keylen = int(sys.argv[3])

space = [i for i in range(256)]
# key = [random.choice(space) for i in range(keylen)]
key = [ord(x) for x in "fisk"]

transform = sys.argv[4]

f = open(path, "r").read()

if transform == 'fish': f = fish(f)
if transform == 'az': f = az(f)

print(f)

f = encode(f, key)

print(f)

f = hexa(f)

print(f)
