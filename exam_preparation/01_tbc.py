def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=' ')

def is_idx_out_of_range(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return True
    return False


def found_area(row, col, matrix):
    if is_idx_out_of_range(row, col, matrix):
        return False
    if matrix[row][col] == 'd':
        return False
    if matrix[row][col] == '*':
        return False

    matrix[row][col] = '*'
    found_area(row - 1, col, matrix)
    found_area(row + 1, col, matrix)
    found_area(row, col - 1, matrix)
    found_area(row, col + 1, matrix)
    found_area(row-1, col + 1, matrix)
    found_area(row-1, col - 1, matrix)
    found_area(row+1, col + 1, matrix)
    found_area(row+1, col - 1, matrix)
    return True


rows = int(input())
cols = int(input())
matrix = []
for _ in range(rows):
    matrix.append(list(input()))
total_paths = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]=='t':
            size = found_area(i, j, matrix)
            # print_matrix(matrix)
            # print('========')
            if size != 0:
                total_paths += 1

print(total_paths)

