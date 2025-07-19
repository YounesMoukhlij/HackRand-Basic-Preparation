from collections import Counter

if __name__ == '__main__':
    number_of_shoes = int(input())
    shoe_size = list(map(int, input().split()))
    number_of_clients = int(input())
    pairs = []
    for _ in range(number_of_clients):
        size, price = map(int, input().split())
        pairs.append((size, price))

    inventory = Counter(shoe_size)
    total = 0

    for size, price in pairs:
        if inventory[size] > 0:
            total += price
            inventory[size] -= 1

    print(total)







# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
