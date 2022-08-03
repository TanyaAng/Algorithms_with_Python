def print_matrix(matrix):
    for row in matrix:
        print(row)


nodes = int(input())
edges = []

for row in range(nodes):
    line = [int(x) for x in input().split()]
    for child in line:
        edges.append((row, child))

# print(edges)
paths_count = int(input())

for _ in range(paths_count):
    is_found_path = True
    current_path = [int(x) for x in input().split()]
    for n in range(0, len(current_path) - 1):
        current_edge = (current_path[n], current_path[n + 1])
        if current_edge not in edges:
            print("no")
            is_found_path = False
            break
    if is_found_path:
        print("yes")
