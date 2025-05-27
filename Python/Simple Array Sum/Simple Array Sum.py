#!/bin/python3

import math
import os
import random
import re
import sys


# This program takes a file from the ENV and calculate the sum of the passed entred numbers
# you need to store the name file or its path in env by doing this in Terminal : export OUTPUT_PATH="name or path"

def simpleArraySum(ar):

    i = 0
    sum = 0
    while i < len(ar):
        sum += ar[i]
        i += 1
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
