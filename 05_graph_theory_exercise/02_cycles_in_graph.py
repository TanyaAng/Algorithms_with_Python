def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(graph):
    for node, dependencies in graph.items():
        if dependencies == 0:
            return node


graph = {}
while True:
    command = input()
    if command == 'End':
        break
    parent, child = command.split('-')
    if parent not in graph:
        graph[parent] = []
    graph[parent].append(child)

graph_dependencies = find_dependencies(graph)

is_acyclic = True
while graph_dependencies:
    node_to_remove = find_node_without_dependencies(graph_dependencies)
    if node_to_remove == None:
        is_acyclic = False
        break
    graph_dependencies.pop(node_to_remove)
    if node_to_remove in graph:
        for child in graph[node_to_remove]:
            if child in graph_dependencies:
                graph_dependencies[child] -= 1

if is_acyclic:
    print("Acyclic: Yes")
else:
    print("Acyclic: No")
