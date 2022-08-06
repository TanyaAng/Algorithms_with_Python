def print_matrix(matrix):
    for row in matrix:
        print(row)


def check_if_row_col_in_range_of_matrix(row, col, matrix):
    if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])):
        return False
    return True


def find_all_paths(row, col, matrix):
    if not check_if_row_col_in_range_of_matrix(row, col, matrix):
        return 0
    if matrix[row][col] == 'd' or matrix[row][col] == 'v':
        return 0
    matrix[row][col] = 'v'
    find_all_paths(row - 1, col, matrix)
    find_all_paths(row + 1, col, matrix)
    find_all_paths(row, col - 1, matrix)
    find_all_paths(row, col + 1, matrix)
    find_all_paths(row - 1, col - 1, matrix)
    find_all_paths(row - 1, col + 1, matrix)
    find_all_paths(row + 1, col - 1, matrix)
    find_all_paths(row + 1, col + 1, matrix)
    return 1


rows = int(input())
cols = int(input())

matrix = []
[matrix.append(list(input())) for _ in range(rows)]

tunnels = 0

for row in range(rows):
    for col in range(cols):
        tunnels += find_all_paths(row, col, matrix)

print_matrix(matrix)
print(tunnels)
