'''
TASK: The graph is directed and unweighted.
SOLUTION: Find the shortest path in unweighted graph and find all nodes, which are not in the path.
IMPLEMENTATION: Shortest path in unweighted graph with start and target not - with BFS and queue.
'''

from collections import deque

nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    first, second = [int(x) for x in input().split()]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    graph[first].append(second)

# print(graph)

start_node = int(input())
target_node = int(input())
visited = {node: False for node in graph}
parent = {node: None for node in graph}
visited[start_node] = True
queue = deque([start_node])
while queue:
    node = queue.popleft()
    if node == target_node:
        break
    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = target_node
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep=' ')

unreached_nodes = []
for key in graph.keys():
    if key not in path:
        unreached_nodes.append(key)
if unreached_nodes:
    print(*sorted(unreached_nodes), sep=' ')
