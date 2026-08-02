def print_rangoli(size):
    alphabets: dict = {
        1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h",
        9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o",
        16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v",
        23: "w", 24: "x", 25: "y", 26: "z"
    }
    width = (size * 4) - 3
    def run_recursion(current_row):
        if current_row >= (size * 2):
            return
        distance_from_center = abs(size - current_row)
        letters_count = size - distance_from_center
        seq = [alphabets[size - i] for i in range(letters_count)]
        mirrored_seq = seq + seq[:-1][::-1]
        line_str = "-".join(mirrored_seq).center(width, '-')
        print(line_str)
        run_recursion(current_row + 1)
    run_recursion(1)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
