def swap_case(s):

    result = ""
    i = 0
    while i < len(s):
        if s[i] >= 'a' and s[i] <= 'z':
            result += chr(ord(s[i]) - 32)
        elif s[i] >= 'A' and s[i] <= 'Z':
            result += chr(ord(s[i]) + 32)
        else:
            result += s[i]
        i += 1
    return result



if __name__ == '__main__':
    s = "HackerRank.com presents \"Pythonist 2\"."
    result = swap_case(s)
    print(result)
