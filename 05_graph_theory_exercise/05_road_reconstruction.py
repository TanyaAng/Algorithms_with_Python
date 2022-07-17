def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = len(children)
    return result


def find_node_with_only_one_path(graph):
    for node, dependencies in graph.items():
        if dependencies == 1:
            return node

#
# def sort_by_paths(graph):
#     sorted_town = {}
#     for key, value in sorted(graph.items(), key=lambda kvp: len(kvp[1])):
#         sorted_town[key] = value
#     return sorted_town


buildings = int(input())
streets = int(input())

town = {}
for _ in range(streets):
    b1, b2 = input().split(' - ')
    if b1 not in town:
        town[b1] = []
    if b2 not in town:
        town[b2] = []
    town[b1].append(b2)
    town[b2].append(b1)

dependencies = find_dependencies(town)
node_with_one_path = find_node_with_only_one_path(dependencies)


nodes_to_remove = []
while town:
    if node_with_one_path == None:
        break
    value_to_remove = town[node_with_one_path][0]
    del town[node_with_one_path]
    for key, values in town.items():
        for v in values:
            if v == node_with_one_path:
                values.remove(v)
    nodes_to_remove.append((value_to_remove, node_with_one_path))
    dependencies = find_dependencies(town)
    node_with_one_path = find_node_with_only_one_path(dependencies)

print("Important streets:")
for node in sorted(nodes_to_remove):
    print(f"{node[0]} {node[1]}")
