# Variant 1
# def dfs(row, col, matrix, value):
#     if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])):
#         return
#     if matrix[row][col] == '*':
#         return
#     if matrix[row][col] != value:
#         return
#     matrix[row][col] = '*'
#     dfs(row + 1, col, matrix, value)
#     dfs(row - 1, col, matrix, value)
#     dfs(row, col - 1, matrix, value)
#     dfs(row, col + 1, matrix, value)
#
#
# n = int(input())
# m = int(input())
#
# matrix = []
# for _ in range(n):
#     matrix.append(list(input()))
# areas = {}
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] != '*':
#             row, col = i, j
#             value = matrix[i][j]
#             dfs(row, col, matrix, value)
#             if value not in areas:
#                 areas[value] = 0
#             areas[value] += 1
#
# print(f"Areas: {sum(areas.values())}")
#
# for key, value in sorted(areas.items()):
#     print(f"Letter '{key}' -> {value}")

# Variant 2
def dfs(row, col, matrix, visited, key):
    if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != key:
        return
    visited[row][col] = True
    dfs(row + 1, col, matrix, visited, key)
    dfs(row - 1, col, matrix, visited, key)
    dfs(row, col - 1, matrix, visited, key)
    dfs(row, col + 1, matrix, visited, key)


n = int(input())
m = int(input())

matrix = []
visited = []
for _ in range(n):
    matrix.append(list(input()))
    visited.append([False] * m)
areas = {}
total_areas = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if visited[i][j]:
            continue
        key = matrix[i][j]
        dfs(i, j, matrix, visited, key)
        if key not in areas:
            areas[key] = 0
        areas[key] += 1
        total_areas += 1

print(f"Areas: {total_areas}")

for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
