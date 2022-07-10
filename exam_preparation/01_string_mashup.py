# def string_mashup(idx, symbols, vector):
#     result=[]
#     if idx >= len(vector):
#         result.append(vector)
#         return
#     for item in symbols:
#         vector[idx] = item
#         string_mashup(idx + 1, symbols, vector)
#     return result
#
#
# symbols = list(input())
# n = int(input())
# vector = [None] * n
# print(string_mashup(0, symbols, vector))

def find_nuclear(idx, collection, vector, used):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for i in range(len(collection)):
        if not used[i]:
            used[i] = True
            vector[idx] = collection[i]
            find_nuclear(idx + 1, collection, vector, used)
            used[i] = False


symbols = sorted(list(input()))
n = int(input())
used = [False] * len(symbols)
vector = [None] * n
find_nuclear(0, symbols, vector, used)
