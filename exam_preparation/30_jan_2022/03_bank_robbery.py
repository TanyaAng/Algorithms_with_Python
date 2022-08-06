def subset_sum(sequence, target, visited, current):
    if sum(current) == target:
        left_sequence = []
        for n in sequence:
            if n not in current:
                left_sequence.append(n)
        if sum(left_sequence) == target:
            print(*sorted(current), sep=' ')
            print(*sorted(left_sequence), sep=' ')
    if sum(current) >= target:
        return
    for i in range(len(sequence)):
        if visited[i]:
            continue
        visited[i] = True
        current.append(sequence[i])
        subset_sum(sequence, target, visited, current)
        visited[-1] = False
        current.pop()



sequence = [int(x) for x in input().split()]
target_sum = sum(sequence) // 2
visited = [False] * len(sequence)
subset_sum(sequence, target_sum, visited, [])
