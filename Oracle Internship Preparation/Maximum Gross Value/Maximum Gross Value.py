def getMax(arr):
    n = len(arr)
    prefix_sum = 0
    best_start = 0
    best_middle = 0
    best_end = 0

    for i in range(n):

        best_start = max(best_start, prefix_sum)
        best_middle = max(best_middle, best_start - prefix_sum)
        best_end = max(best_end, best_middle + prefix_sum)

        if i < n:
            prefix_sum += arr[i]

    return 2 * best_end - sum(arr)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    print(getMax(arr))
