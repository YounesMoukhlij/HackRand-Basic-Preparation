if __name__ == "__main__":

    thickness = int(input())
    c = 'H'

    # top triangle
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # top rectangle
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # middle belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # bottom rectangle
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # bottom triangle (fixed)
    j = thickness - 1
    while j >= 0:
        print(  ((c * j).rjust(thickness - 1) + c + (c * j).ljust(thickness)).rjust(thickness * 6))
        j -= 1
