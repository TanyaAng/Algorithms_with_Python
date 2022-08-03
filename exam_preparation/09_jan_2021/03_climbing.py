def print_matrix(matrix):
    for idx, row in enumerate(matrix):
        print(f"{idx} - {row}")


rows = int(input())
cols = int(input())

matrix = []
dp = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + matrix[row][col]

row = rows - 1
col = cols - 1
result = []
path = []
while row > 0 and col > 0:
    result.append(matrix[row][col])
    path.append((row, col))
    if dp[row][col - 1] > dp[row - 1][col]:
        col -= 1
    elif dp[row][col - 1] < dp[row - 1][col]:
        row -= 1
    elif dp[row][col - 1] == dp[row - 1][col]:
        row -= 1

while col > 0:
    result.append(matrix[row][col])
    path.append((row, col))
    col -= 1

while row > 0:
    result.append(matrix[row][col])
    path.append((row, col))
    row -= 1

# print_matrix(dp)
print(dp[rows - 1][cols - 1])
result.append(matrix[0][0])
# path.append((0, 0))
print(*result, sep=' ')
# print(*path, sep=' ')
