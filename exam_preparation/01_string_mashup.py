def is_lexicographical_order(array):
    if sorted(array) == array:
        return True
    return False


def find_nuclear(idx, collection, vector):
    if idx >= len(vector):
        if is_lexicographical_order(vector):
            print(*vector, sep='')
        return
    for i in range(len(collection)):
        vector[idx] = collection[i]
        find_nuclear(idx + 1, collection, vector)


symbols = sorted(list(input()))
n = int(input())
used = [False] * len(symbols)
vector = [None] * n
find_nuclear(0, symbols, vector)
