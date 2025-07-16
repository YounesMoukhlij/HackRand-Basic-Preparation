

def split_and_join(line):

    test = line.split(' ')
    result = "-".join(test)


    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
