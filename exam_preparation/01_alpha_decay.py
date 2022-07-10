# VARIANT 1
# def is_unique_elements(collection):
#     if len(collection) == len(set(collection)):
#         return True
#     return False


# def find_nuclear(idx, collection, vector):
#     if idx >= len(vector) and is_unique_elements(vector):
#         print(*vector, sep=' ')
#         return
#     if idx >= len(vector) and not is_unique_elements(vector):
#         return
#     for item in collection:
#         vector[idx] = item
#         find_nuclear(idx + 1, collection, vector)

# VARIANT 2
def find_nuclear(idx, collection, vector, used):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return
    for i in range(len(collection)):
        if not used[i]:
            used[i] = True
            vector[idx] = collection[i]
            find_nuclear(idx + 1, collection, vector, used)
            used[i] = False


numbers = input().split()
n = int(input())
used = [False] * len(numbers)
vector = [None] * n
find_nuclear(0, numbers, vector, used)
