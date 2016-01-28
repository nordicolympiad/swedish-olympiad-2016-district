#!/usr/bin/env python3

import sys
import string
t, msg = input().split()
if t != "3": sys.exit(0)

nmsg = []
ans = []

while msg:
    for i in range(len(msg)):
        if i % 2 == 0:
            ans += [msg[i]]
        else:
            nmsg += [msg[i]]
    msg = list(reversed(nmsg))
    nmsg = []

print(''.join(ans));
