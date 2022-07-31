from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight, connected=False):
        self.source = source
        self.destination = destination
        self.weight = weight
        self.connected = connected

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)
    pq = PriorityQueue()
    for edge in graph[node]:
        if not edge.connected:
            pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = None
        if min_edge.source in forest and min_edge.destination not in forest:
            non_tree_node = min_edge.destination

        elif min_edge.source not in forest and min_edge.destination in forest:
            non_tree_node = min_edge.source
        if non_tree_node == None:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)
        for edge in graph[non_tree_node]:
            if not edge.connected:
                pq.put(edge)


budget = int(input())
nodes = int(input())
edges = int(input())

graph = {}
visited = set()
initially_connected = set()
for _ in range(edges):
    line = input().split()
    source, destination, weight = [int(x) for x in line[0:3]]
    if len(line) == 4:
        edge = Edge(source, destination, weight, connected=True)
        if source not in initially_connected:
            initially_connected.add(source)
        if destination not in initially_connected:
            initially_connected.add(destination)
    else:
        edge = Edge(source, destination, weight, connected=False)
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(edge)
    graph[destination].append(edge)

forest = set()
forest_edges = []
for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

budget_used = 0

connections = []
for edge in sorted(forest_edges, key=lambda x: x.weight):

    if edge.source in initially_connected and edge.destination not in initially_connected and budget_used + edge.weight <= budget:
        initially_connected.add(edge.destination)
        budget_used += edge.weight
        connections.append(edge)
    elif edge.source not in initially_connected and edge.destination in initially_connected and budget_used + edge.weight <= budget:
        initially_connected.add(edge.source)
        budget_used += edge.weight
        connections.append(edge)

print(f"Budget used: {budget_used}")
