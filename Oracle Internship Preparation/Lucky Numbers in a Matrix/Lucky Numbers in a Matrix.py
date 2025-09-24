
r, c = map(int, input().split())

matrix = []
if not (c > 50 or r < 1):
    for _ in range (r):
        row = input().split()
        new = []
        for x in row:
            new.append(int(x))
        matrix.append(new)



    res = []

    for i in range(r):
        row_min_value = min(matrix[i])
        index_column = matrix[i].index(row_min_value)
        max_col = matrix[0][index_column]
        for o in range(r):
            if matrix[o][index_column] > max_col:
                max_col = matrix[o][index_column]

        if row_min_value == max_col:
            res.append(row_min_value)



    if res:
        print(res[0])
    else :
        print()


