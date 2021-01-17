#!/usr/bin/python3

# Test script for the script module in Ansible

import math
import sys
from random import randrange as r
print('A slice of pi:',str(math.pi)[0:6])
print('A random number:',r(0,4096))
try:
    print(sys.argv[1],'|  Yay, an argument. :)')
except Exception:
    print('No argument given :(')
