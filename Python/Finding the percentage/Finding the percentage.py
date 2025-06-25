if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        scores = student_marks[query_name]
        sum = 0
        i = 0

        while i < len(scores):
            sum += scores[i]
            i += 1
        sum = sum / len(scores)

        print(f"{sum:.2f}")

