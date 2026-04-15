def average(array):


    newArray = set(float(x) for x in array)
    res = sum(newArray) / float(len(newArray))


    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

