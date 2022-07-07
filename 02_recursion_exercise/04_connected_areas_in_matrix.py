class Area():
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def is_idx_out_of_range(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return True
    return False


def explode_area(row, col, matrix):
    if is_idx_out_of_range(row, col, matrix):
        return 0
    if matrix[row][col] == '*':
        return 0
    if matrix[row][col] == 'v':
        return 0

    matrix[row][col] = 'v'
    result = 1
    result += explode_area(row - 1, col, matrix)
    result += explode_area(row + 1, col, matrix)
    result += explode_area(row, col + 1, matrix)
    result += explode_area(row, col - 1, matrix)
    return result


rows = int(input())
cols = int(input())
matrix = []

for i in range(rows):
    matrix.append(list(input()))

total_areas = 0
result = []
for row in range(rows):
    for col in range(cols):
        size = explode_area(row, col, matrix)
        if size == 0:
            continue
        result.append(Area(row, col, size))

print(f"Total areas found: {len(result)}")
for idx, area in enumerate(sorted(result, key=lambda a: a.size, reverse=True)):
    print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")
