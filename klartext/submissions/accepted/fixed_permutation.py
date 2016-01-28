#!/usr/bin/env python3

import sys
import string
t, msg = input().split()
if t != "2": sys.exit(0)

perm = [
        24, 21, 23, 20, 22,
        9, 6, 8, 5, 7,
        19, 16, 18, 15, 17,
        4, 1, 3, 0, 2,
        14, 11, 13, 10, 12
]

nmsg = ''.join([msg[perm[i]] for i in range(25)])
print(nmsg)
