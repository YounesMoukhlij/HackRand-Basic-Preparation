if __name__ == '__main__':
    n = int(input())
    r = []
    mainList = []
    for _ in range(n):

        name = input()
        score = float(input())
        r = [name, score]
        mainList.append(r)


    mainList.sort()


    numbers = []
    for i in range(n):
        numbers.append(mainList[i][1])

    numbers.sort()
    check = numbers[0]

    for i in range(n):
        if check < numbers[i]:
            check = numbers[i]
            break



    for j in range(n):
        if mainList[j][1] == check:
            print(mainList[j][0])
