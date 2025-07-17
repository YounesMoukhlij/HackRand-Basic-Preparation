#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):

    i = 0

    new = ""
    while i < len(s):

        if (s[i - 1].isspace() or i == 0) and (s[i] >= 'a' and s[i] <= 'z') :
            new += chr(ord(s[i]) - 32)
        else:
            new += s[i]
        i += 1

    return new



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
