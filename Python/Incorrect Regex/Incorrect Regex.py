import re

def is_valid_regex(pattern):
    # Check for multiple repeat errors first
    for i in range(len(pattern) - 1):
        if pattern[i] in '*+?}' and pattern[i+1] in '*+?{':
            return False
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

n = int(input())
for _ in range(n):
    s = input().strip()
    print(is_valid_regex(s))
