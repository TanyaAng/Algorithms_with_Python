from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]
tree = set()

for _ in range(edges):
    line = input().split()
    source, destination, weight = [int(x) for x in line[0:3]]
    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)
    if len(line) == 4:
        tree.add(source)
        tree.add(destination)

pq = PriorityQueue()

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

budget_used = 0
while not pq.empty():
    min_edge = pq.get()
    non_tree_node = None
    if min_edge.source in tree and min_edge.destination not in tree:
        non_tree_node = min_edge.destination
    elif min_edge.source not in tree and min_edge.destination in tree:
        non_tree_node = min_edge.source

    if non_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break
    budget_used += min_edge.weight
    tree.add(non_tree_node)
    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f"Budget used: {budget_used}")
