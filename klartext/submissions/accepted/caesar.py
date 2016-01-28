#!/usr/bin/env python3

import sys
import string
t, msg = input().split()
if t != "1": sys.exit(0)
shift, msg = msg.split("-")
shift = int(shift)
A = string.ascii_lowercase
print(''.join(A[(int(shift) + A.find(i)) % len(A)] for i in msg))
