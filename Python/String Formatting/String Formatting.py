def print_formatted(number):

    width = len(bin(number)[2:])

    i = 1
    while i <= number:
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")
        i += 1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
