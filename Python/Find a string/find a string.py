def count_substring(string, sub_string):
    li = 0
    i = 0

    while i <= len(string) - len(sub_string):
        j = 0
        while j < len(sub_string) and string[i + j] == sub_string[j]:
            j += 1
        if j == len(sub_string):
            li += 1
        i += 1

    # solution 2
    # while i < len(string):
    #     j = 0
    #     if string[i] == sub_string[j]:
    #         while j < len(sub_string) and (i + j) < len(string) and string[i + j] == sub_string[j]:
    #             j += 1

    #     if j == len(sub_string):
    #         li += 1
    #     i += 1
    return li

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
