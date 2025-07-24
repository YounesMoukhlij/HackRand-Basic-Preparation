
if __name__ == "__main__":

    o = int(input())

    all_cases = []

    for _ in range(o):
        ar = list(map(str, input().split()))
        all_cases.append(ar)

    i = 0
    while i < o:
        try:
            case = all_cases[i]
            a, b = case[0], case[1]
            if int(b) == 0:
                raise ZeroDivisionError("Error Code: integer division or modulo by zero")
            if  not a.isdigit():
                raise ValueError(f"invalid literal for int() with base 10: '{a}'")
            if  not b.isdigit():
                raise ValueError(f"invalid literal for int() with base 10: '{b}'")
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code: " + str(e))
        i += 1
