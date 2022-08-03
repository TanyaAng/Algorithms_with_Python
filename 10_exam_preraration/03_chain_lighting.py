from collections import deque


def print_graph(graph):
    for idx, node in enumerate(graph):
        print(f"Node: {idx}")
        for edge in node:
            print(edge.__dict__)


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


def bfs(node, graph, visited, damage, force, start_node):
    if visited[node]:
        return
    if node == start_node:
        damage[node] += force
    queue = deque([node])
    visited[node] = True
    while queue:
        current_node = queue.popleft()
        # print(current_node, end=' ')
        for child in graph[current_node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                if current_node == start_node:
                    damage[child] += force / 2
                else:
                    damage[child] += force / 4


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


nodes = int(input())
edges = int(input())
lighting = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)
    graph.append(edge)

thunderstorms = []
for _ in range(lighting):
    start_node, force = [int(x) for x in input().split()]
    thunderstorms.append((start_node, force))

parent = {num: num for num in range(nodes)}
min_spanning_tree = []

for edge in sorted(graph, key=lambda e: e.weight):
    first = find_root(parent, edge.source)
    second = find_root(parent, edge.destination)
    if first != second:
        parent[first] = second
        min_spanning_tree.append((edge.source, edge.destination))

# print(f"Minimum spannig_tree: {min_spanning_tree}")

parent_children_graph = {}
for edge in min_spanning_tree:
    if edge[0] not in parent_children_graph:
        parent_children_graph[edge[0]] = []
    parent_children_graph[edge[0]].append(edge[1])
    if edge[1] not in parent_children_graph:
        parent_children_graph[edge[1]] = []
    parent_children_graph[edge[1]].append(edge[0])

# print(f"Parent - child graph: {parent_children_graph}")

damage = {node: 0 for node in parent_children_graph}

for thunder in thunderstorms:
    visited = {node: None for node in parent_children_graph}
    start_node, force = thunder
    new_graph = {}
    new_graph[start_node] = parent_children_graph[start_node]
    for node in parent_children_graph:
        if node not in new_graph:
            new_graph[node] = parent_children_graph[node]
    # print(f"New graph: {new_graph}\n")
    for node in new_graph:
        bfs(node, parent_children_graph, visited, damage, force, start_node)

print(int(max(damage.values())))
