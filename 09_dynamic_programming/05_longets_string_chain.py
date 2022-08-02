from collections import deque

string_chain = input().split()
lenght_chain = [len(string) for string in string_chain]

lenght = len(string_chain)

size = [0] * lenght
size[0] = 1
parent = [None] * lenght

best_idx = 0
best_size = 1

for idx in range(1, lenght):
    current_chain = lenght_chain[idx]
    current_best_size = 1
    current_parrent = None

    for prev in range(idx - 1, -1, -1):
        prev_chain = lenght_chain[prev]

        if prev_chain >= current_chain:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parrent = prev

    size[idx] = current_best_size
    parent[idx] = current_parrent
    if current_best_size > best_size:
        best_size = current_best_size
        best_idx = idx

result = deque()
while best_idx is not None:
    result.appendleft(string_chain[best_idx])
    best_idx = parent[best_idx]

print(*result, sep=' ')
