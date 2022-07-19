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

total_salaries = 0

for node in graph.keys():
    total_salaries += dfs(node, graph)

print(f"{total_salaries}")
