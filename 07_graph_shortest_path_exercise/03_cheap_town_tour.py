class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


nodes = int(input())
edges = int(input())

graph = []
nodes_list = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(' - ')]
    graph.append(Edge(source, destination, weight))
    if source not in nodes_list:
        nodes_list.append(source)
    if destination not in nodes_list:
        nodes_list.append(destination)

for edge in sorted(graph, key=lambda e: e.weight):
    print(edge.__dict__)

parent = {node: node for node in nodes_list}
# print(parent)

min_spanning_tree = []

for edge in sorted(graph, key=lambda x: x.weight):
    first = find_root(parent, edge.source)
    second = find_root(parent, edge.destination)
    if first != second:
        parent[first] = second
        min_spanning_tree.append(edge)

# for edge in min_spanning_tree:
#     print(edge.__dict__)

total_cost = sum([edge.weight for edge in min_spanning_tree])
print(f"Total cost: {total_cost}")
