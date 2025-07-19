if __name__ == '__main__':
    a = int(input())
    b = int(input())

    mytuple = (a // b, a % b)


    i = 0
    while i < len(mytuple):
        print(mytuple[i])
        i += 1
    print(mytuple)


