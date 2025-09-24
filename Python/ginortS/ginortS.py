


def sort_key(character):
    if character.islower():
        return (0, character)
    elif character.isupper():
        return (1, character)
    elif character.isdigit():
        d = int(character)
        if d % 2 == 1:
            return (2, d)
        else:
            return (3, d)

if __name__ == '__main__':

    s = str(input())


    if s.isalnum():
        print(''.join(sorted(s, key=sort_key)))
