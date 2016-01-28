#!/usr/bin/env python3

import sys
import string
t, msg = input().split()
if t != "4": sys.exit(0)

def generate(a, b):
    if b - a == 1:
        return [a]

    mid = (a + b) // 2
    if (b - a) % 2 == 0:
        return generate(mid, b) + generate(a, mid)
    return generate(a, mid) + [mid] + generate(mid + 1, b)

perm = generate(0, len(msg))

nmsg = ''.join([msg[perm[i]] for i in range(len(msg))])
print(nmsg)
