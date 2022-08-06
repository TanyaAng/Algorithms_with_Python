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

print(graph)

total_salaries = 0

for node in graph.keys():
    total_salaries += dfs(node, graph)

print(f"{total_salaries}")


# VARIANT 2
# def dfs(node, graph, salaries):
#     if salaries[node] is not None:
#         return salaries[node]
#     if len(graph[node]) == 0:
#         salaries[node] = 1
#         return 1
#     salary = 0
#     for child in graph[node]:
#         salary += dfs(child, graph, salaries)
#     salaries[node] = salary
#     return salary
#
#
# n = int(input())
#
# graph = []
# for _ in range(n):
#     line = input()
#     children = []
#     for idx, state in enumerate(line):
#         if state == 'Y':
#             children.append(idx)
#     graph.append(children)
#
# salaries = [None] * n
#
# result = 0
# for node in range(len(graph)):
#     salary = dfs(node, graph, salaries)
#     result += salary
#
# print(result)
