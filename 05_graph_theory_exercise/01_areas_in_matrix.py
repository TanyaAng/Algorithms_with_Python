def dfs(row, col, matrix, value):
    if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])):
        return
    if matrix[row][col] == '*':
        return
    if matrix[row][col] != value:
        return
    matrix[row][col] = '*'
    dfs(row + 1, col, matrix, value)
    dfs(row - 1, col, matrix, value)
    dfs(row, col - 1, matrix, value)
    dfs(row, col + 1, matrix, value)


n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))
areas = {}

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != '*':
            row, col = i, j
            value = matrix[i][j]
            dfs(row, col, matrix, value)
            if value not in areas:
                areas[value] = 0
            areas[value] += 1

print(f"Areas: {sum(areas.values())}")

for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
