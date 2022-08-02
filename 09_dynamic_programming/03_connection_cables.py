# VARIANT I - Longest Increasing Subsequence
# cables = [int(x) for x in input().split()]
#
# lenght = len(cables)
# size = [0] * lenght
# size[0] = 1
# best_size = 1
# for idx in range(1, lenght):
#     cable = cables[idx]
#     current_best_size = 1
#
#     for prev in range(idx - 1, -1, -1):
#         prev_cable = cables[prev]
#         if prev_cable >= cable:
#             continue
#
#         if size[prev] + 1 >= current_best_size:
#             current_best_size = size[prev] + 1
#
#     size[idx] = current_best_size
#
#     if current_best_size > best_size:
#         best_size = current_best_size
#
# print(f"Maximum pairs connected: {best_size}")


# VARIANT II - Longest Common Subsequence
cables = [int(x) for x in input().split()]
size = len(cables) + 1

positions = [pos for pos in range(1, size)]

lcs = []
[lcs.append([0] * size) for _ in range(size)]

for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == positions[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])

print(f"Maximum pairs connected: {lcs[size - 1][size - 1]}")
