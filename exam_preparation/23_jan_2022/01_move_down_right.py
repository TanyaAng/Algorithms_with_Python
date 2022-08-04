def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=' ')

def check_if_row_col_in_range_of_matrix(row, col, matrix):
    if row not in range(0, len(matrix)) or col not in range(0, len(matrix[0])):
        return False
    return True


def move_down_right(row, col, matrix):
    if not check_if_row_col_in_range_of_matrix(row, col, matrix):
        return 0
    if matrix[row][col] == '*':
        return 0
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        return 1
    result = 0
    matrix[row][col] = '*'
    result += move_down_right(row, col + 1, matrix)
    result += move_down_right(row + 1, col, matrix)
    matrix[row][col] = '-'
    return result


rows = int(input())
cols = int(input())

matrix = []

[matrix.append(['-'] * cols) for _ in range(rows)]

# for row in matrix:
#     print(*row, sep=' ')

start_row = 0
start_col = 0
print(move_down_right(start_row, start_col, matrix))
