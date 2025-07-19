

def palindromeTriangle(num, filename):

    i = 1
    with open(filename, 'w') as file:
        while i <= num:
            j = 1
            tmp = i % num
            if tmp == 0:
                tmp = num
            line = ""
            while tmp > 0:
                line += "%d" % j
                j += 1
                if j == i % num or j == num:
                    while j > 0:
                        line += "%d" % j
                        j -= 1
                    break
                tmp -= 1
            file.write(line)
            if i < num:
                file.write('\n')
            i += 1
    file.close()
    return


if __name__ == '__main__':

    num = int(input())


    palindromeTriangle(num, "output.txt")
    with open("output.txt", 'r') as f:
        print(f.read())
        f.close()




# if n = 5
# ----- result -----
# 1
# 121
# 12321
# 1234321
# 123454321
