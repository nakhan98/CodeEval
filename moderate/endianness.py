#!/usr/bin/env python2
'''
- CodeEval: Endianness
- https://www.codeeval.com/open_challenges/15/
'''

from sys import byteorder

if byteorder == "little":
    print("LittleEndian")
else:
    print("BigEndian")

