def recursive_nested_loops(n, vector, idx=0):
    if idx >= len(vector):
        print(*vector, sep=' ')
        return
    for i in range(1, n + 1):
        vector[idx] = i
        recursive_nested_loops(n, vector, idx + 1)


n = int(input())
vector = ['-'] * n
recursive_nested_loops(n, vector)
