


graph = [[1], [2, 3], [3], [4], []]
dependencies_by_node = find_dependencies(graph)
print(dependencies_by_node)
print(find_path(graph, dependencies_by_node))


print('========')

graph = [[1], [3], [4], []]
dependencies_by_node = find_dependencies(graph)
print(dependencies_by_node)
print(find_path(graph, dependencies_by_node))


