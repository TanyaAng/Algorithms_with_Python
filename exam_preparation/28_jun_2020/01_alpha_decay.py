def alpha_decay(idx, sequence, vector, visited):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return
    for i in range(len(sequence)):
        if visited[i]:
            continue
        visited[i] = True
        vector[idx] = sequence[i]
        # print(f"=====> Pre-recursion: {vector}")
        alpha_decay(idx + 1, sequence, vector, visited)
        # print(f"=====> Post-recursion: {vector}")
        visited[i]=False


sequence = [int(x) for x in input().split()]
n = int(input())
vector = [''] * n
visited = [False] * len(sequence)
alpha_decay(0, sequence, vector, visited)
