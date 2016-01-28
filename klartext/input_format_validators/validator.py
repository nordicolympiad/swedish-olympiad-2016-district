#!/usr/bin/env python3

import sys
import string
t, msg = input().split()

if t == "1":
    caesar(msg)
elif t == "2":
    fixed(msg)
elif t == "3":
    railgun(msg)
elif t == "4":
    dynamic(msg)
elif t == "5":
    code(msg)
else:
    assert False, "bad cipher"

sys.exit(42)
