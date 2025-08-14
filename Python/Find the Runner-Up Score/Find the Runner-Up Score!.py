if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_sorted = sorted(set(arr))

    print(arr_sorted[len(arr_sorted) - 2])

