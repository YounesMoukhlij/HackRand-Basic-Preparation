if __name__ == "__main__":
    n = int(input())


    arr = tuple(map(int, input().split()))[:n]

    arr = tuple(arr)

    print(hash(arr))
