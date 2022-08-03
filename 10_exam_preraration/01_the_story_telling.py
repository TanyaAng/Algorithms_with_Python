from collections import deque


def dfs(node, graph, visited, the_whole_story):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited, the_whole_story)
    the_whole_story.appendleft(node)


graph = {}

command = input()
while command != 'End':
    stories = command.split('->')
    if len(stories) == 1:
        prestory = stories[0].strip()
        if prestory not in graph:
            graph[prestory] = []

    else:
        prestory = stories[0].strip()
        poststories = stories[1].split()
        if prestory not in graph:
            graph[prestory] = []
        graph[prestory] = poststories
    command = input()

visited = set()
the_whole_story = deque()
for node in graph:
    dfs(node, graph, visited, the_whole_story)

print(*the_whole_story, sep=' ')
