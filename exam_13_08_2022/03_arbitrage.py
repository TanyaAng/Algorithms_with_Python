from collections import deque
from queue import PriorityQueue


def find_path(parent, destination):
    path = deque()
    node = destination
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


class Edge:
    def __init__(self, first, second, price):
        self.first = first
        self.second = second
        self.price = price


traiding_pairs = int(input())

graph = {}
nodes = set()

for _ in range(traiding_pairs):
    first, second, price = input().split()
    price_as_float = float(price)
    edge = Edge(first, second, price_as_float)
    nodes.add(first)
    nodes.add(second)
    if first not in graph:
        graph[first] = []
    graph[first].append(edge)

start = input()

prices = {node: float('-inf') for node in nodes}
prices[start] = 1
parent = {node: None for node in nodes}
pq = PriorityQueue()
pq.put((-1, start))
max_price = 0
is_found_start = False
destination = None
while not pq.empty():
    max_price, node = pq.get()
    max_price = abs(max_price)
    if node not in graph:
        continue
    for edge in graph[node]:
        new_price = max_price * edge.price
        if new_price > prices[edge.second]:
            prices[edge.second] = new_price
        if edge.second == start:
            destination = edge.first
            is_found_start = True
            break
        parent[edge.second] = node
        pq.put((-new_price, edge.second))
    if is_found_start:
        break

if prices[start] > 1:
    print("True")
    path = find_path(parent, destination)
    path.append(start)
    print(*path, sep=' ')
else:
    print("False")
    path = find_path(parent, destination)
    for node in path:
        print(f"{node}: {prices[node]:.3f}")
