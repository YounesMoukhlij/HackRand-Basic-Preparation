
def minion_game(string):

    vowels = set("AUIOE")
    kevinScore = 0
    stuartScore = 0

    remaining = 0
    for index, char in enumerate(string):
        remaining = len(string) - index
        if char in vowels:
            kevinScore += remaining
        else:
            stuartScore += remaining

    if kevinScore > stuartScore:
        print("Kevin", kevinScore)
    else:
        print("Stuart", stuartScore)



if __name__ == '__main__':
    s = input()
    minion_game(s)























# My Old answer, it take too much time to execute

# def kevinFunction(string):
#     voweles = ['A', 'E' , 'I' , 'O' , 'U', 'a', 'u', 'i', 'o', 'e']
#     stringList = []
#     i = 0
#     score = 0
#     while i < len(string):
#         if string[i] in voweles:
#             j = 0
#             while j < len(string):
#                 j += 1
#                 if string[i:j] not in stringList and i < j:
#                     stringList.append(string[i:j])
#                     score += 1
#                 else:
#                     score += searchSubStrings(string, string[i:j])
#         i += 1
#     return score


# def searchSubStrings(string, subString):
#     i = string.find(subString)

#     if i:
#         return 1
#     return 0


# def stuartFunction(string):
#     voweles = ['A', 'E' , 'I' , 'O' , 'U', 'a', 'u', 'i', 'o', 'e']
#     stringList = []
#     i = 0
#     score = 0
#     while i < len(string):
#         if string[i] not in voweles:
#             j = 0
#             while j < len(string):
#                 j += 1
#                 if string[i:j] not in stringList and i < j:
#                     stringList.append(string[i:j])
#                     score += 1
#                 else:
#                     score += searchSubStrings(string, string[i:j])
#         i += 1
#     return score


# def minion_game(string):
#     stuartScore = stuartFunction(string)
#     kevinScore = kevinFunction(string)

#     if stuartScore > kevinScore:
#         print("Stuart", stuartScore)
#     else:
#         print("Kevin", kevinScore)


# if __name__ == '__main__':
#     # s = input()

#     s = "BANAASA"

#     minion_game(s)
