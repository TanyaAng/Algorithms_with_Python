def find_dependecies(graph):
    result = {}
    for node, childer in graph.items():
        if node not in result:
            result[node] = 0
        for child in childer:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_without_without_dependecies(dependencies_by_node):
    for node, dependecies in dependencies_by_node.items():
        if dependecies == 0:
            return node
    return None


nodes = int(input())

graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

#print(graph)

dependencies_by_node = find_dependecies(graph)
#print(dependencies_by_node)

has_cycles = False
sorted_nodes = []
while dependencies_by_node:
    node_to_remove = find_without_without_dependecies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

