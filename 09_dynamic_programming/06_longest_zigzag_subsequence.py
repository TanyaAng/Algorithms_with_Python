from collections import deque
sequence = [int(x) for x in input().split()]

lenght = len(sequence)
size = [0] * lenght
parent = [None] * lenght
parent[0]=sequence[0]

size[0] = 1
best_idx = 0
bes_size = 0

for idx in range(1, lenght):
    current_number = sequence[idx]
    current_best_size = 1
    current_parent = None

    for prev in range(idx - 1, -1, -1):
        prev_number = sequence[prev]

        if prev_number >= current_number:
            parent[prev]=sequence[prev]
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1
            current_parent = sequence[prev]

    size[idx] = current_best_size
    parent[idx] = current_parent
    if current_best_size > bes_size:
        best_size = current_best_size
        best_idx = idx

print(sequence)
print(size)
print(best_idx)
print(parent)

# result=deque()
# while best_idx is not None:
#     result.appendleft(sequence[best_idx])
#     best_idx=parent[best_idx]
#
# print(*result, sep=' ')