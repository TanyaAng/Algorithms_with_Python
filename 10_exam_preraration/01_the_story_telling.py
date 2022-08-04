from collections import deque


# VARIANT I - WITH DFS
# def dfs(node, graph, visited, the_whole_story):
#     if node in visited:
#         return
#     visited.add(node)
#     for child in graph[node]:
#         dfs(child, graph, visited, the_whole_story)
#     the_whole_story.appendleft(node)
#
#
# graph = {}
#
# command = input()
# while command != 'End':
#     stories = command.split('->')
#     if len(stories) == 1:
#         prestory = stories[0].strip()
#         if prestory not in graph:
#             graph[prestory] = []
#
#     else:
#         prestory = stories[0].strip()
#         poststories = stories[1].split()
#         if prestory not in graph:
#             graph[prestory] = []
#         graph[prestory] = poststories
#     command = input()
#
# visited = set()
# the_whole_story = deque()
# for node in graph:
#     dfs(node, graph, visited, the_whole_story)
#
# print(*the_whole_story, sep=' ')


# VARIANT II - TOPOLOGICAL SORTING WITH DFS
def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)
    result.appendleft(node)


graph = {}

command = input()
while command != 'End':
    args = command.split('->')
    if len(args) == 1:
        parent = args[0].strip()
        if parent not in graph:
            graph[parent] = []

    else:
        parent = args[0].strip()
        children = args[1].split()
        if parent not in graph:
            graph[parent] = []
        graph[parent] = children
    command = input()

result = deque()
visited = set()
for node in graph:
    dfs(node, graph, visited, result)

print(*result, sep=' ')
