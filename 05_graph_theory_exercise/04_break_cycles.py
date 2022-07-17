def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = len(children)
    return result


def find_node_with_only_one_path(graph):
    for node, dependencies in graph.items():
        if dependencies > 1:
            return node


def sort_by_paths(graph):
    sorted_graph = {}
    for key, value in sorted(graph.items(), key=lambda kvp: -len(kvp[1])):
        sorted_graph[key] = value
    return sorted_graph


n = int(input())

graph = {}
for _ in range(n):
    command = input()
    parent, children = command.split('->')
    parent = parent.strip()
    if parent not in graph:
        graph[parent] = []
    children = children.strip()
    graph[parent] = children.split()

sorted_graph = sort_by_paths(graph)
print(sorted_graph)
dependencies = find_dependencies(sorted_graph)
print(dependencies)
node_with_many_paths = find_node_with_only_one_path(dependencies)

has_cycles = True
nodes_to_remove = []
while graph:
    if node_with_many_paths == None:
        has_cycles = False
        break
    value_to_remove = graph[node_with_many_paths][0]
    del graph[node_with_many_paths]
    for key, values in graph.items():
        for v in values:
            if v == node_with_many_paths or v == value_to_remove:
                values.remove(v)
    nodes_to_remove.append((value_to_remove, node_with_many_paths))
    dependencies = find_dependencies(graph)
    node_with_many_paths = find_node_with_only_one_path(dependencies)

print("Important streets:")
for node in sorted(nodes_to_remove):
    print(f"{node[0]} {node[1]}")
