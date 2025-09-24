import textwrap

def wrap(string, max_width):

    j = 0
    s = ""
    for i in range(len(string)):
        s += string[i]
        j += 1
        if j == max_width:
            s += '\n'
            j = 0
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
