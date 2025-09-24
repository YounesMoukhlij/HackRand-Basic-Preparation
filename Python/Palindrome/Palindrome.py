if __name__ == "__main__":
    s = str(input())

    i = 0
    j = 0

    while i < len(s):
        if s[i] == s[len(s) - i - 1]:
            j += 1
        i += 1

    if j == len(s):
        print("Good")
    else:
        print("Bad")

