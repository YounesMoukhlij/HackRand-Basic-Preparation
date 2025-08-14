if __name__ == '__main__':

    l = []

    while True:
        try:
            line = input()
            if line == '':
                break
            a, b = line.split()
            l.append((int(a),int(b)))
        except EOFError:
            break

    i = 0
    while i < len(l):
        print(l[i])
        i += 1

    result = []
    for i in l:
        result.append())
    print(' '.join(result))


# A = [1, 2]
# B = [3, 4]
