
if __name__ == '__main__':
    size = int(input())

    with open("output.txt", "w+") as f:
        i = 1
        line = ""
        while i < size:
            tmp = i % size
            j = 1
            while j <= tmp:
                line += "%d" % i
                j += 1
            if i <= size:
                f.write(line + '\n')
            line = ""
            i += 1
        f.seek(0)
        print(f.read(), end="")
        f.close()
        