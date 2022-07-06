def print_matrix(matrix):
    for row in range(len(matrix)):
        print(' '.join([matrix[row][col] for col in range(len(matrix[0]))]))


def is_idx_out_of_range(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return True
    return False


def calculate_total_paths_to_end_point(row, col, matrix, end_row, end_col, counter=[]):
    if is_idx_out_of_range(row, col, matrix) or matrix[row][col] == '*':
        return
    if row == end_row and col == end_col:
        matrix[row][col] = '*'
        counter.append(1)
        matrix[row][col] = '-'
    else:
        # mark cells
        matrix[row][col] = '*'
        calculate_total_paths_to_end_point(row + 1, col, matrix, end_row, end_col, counter=counter)
        calculate_total_paths_to_end_point(row, col + 1, matrix, end_row, end_col, counter=counter)
        # unmark cells
        matrix[row][col] = '-'

    return len(counter)


m = int(input())
n = int(input())
matrix = []

for i in range(m):
    matrix.append(['-' for j in range(n)])
# print_matrix(matrix)
start_point = (0, 0)
end_row, end_col = m - 1, n - 1

print(calculate_total_paths_to_end_point(0, 0, matrix, end_row, end_col))
