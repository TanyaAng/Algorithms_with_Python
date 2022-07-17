def find_dependencies(matrix):
    result = {}
    for i in range(len(matrix)):
        if i not in result:
            result[i] = 0
        for j in range(len(matrix)):
            if matrix[i][j] == 'Y':
                if j not in result:
                    result[j] = 1
                else:
                    result[j] += 1
    return result


def dfs(node, graph):
    if graph[node] == []:
        return 1
    current_salaries = 0
    for child in graph[node]:
        current_salaries += dfs(child, graph)
    return current_salaries


n = int(input())
employee_matrix = []
for _ in range(n):
    employee_matrix.append(list(input()))

graph = {}
for i in range(n):
    graph[i] = []
    for j in range(n):
        if employee_matrix[i][j] == 'Y':
            graph[i].append(j)

dependencies = find_dependencies(employee_matrix)
total_salaries = 0

for node in graph.keys():
    total_salaries += dfs(node, graph)

print(f"{total_salaries}")
