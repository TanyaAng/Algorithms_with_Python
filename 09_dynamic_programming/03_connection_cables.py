cables = [int(x) for x in input().split()]

lenght = len(cables)
size = [0] * lenght
size[0] = 1
best_size = 1
for idx in range(1, lenght):
    cable = cables[idx]
    current_best_size = 1

    for prev in range(idx - 1, -1, -1):
        prev_cable = cables[prev]
        if prev_cable >= cable:
            continue

        if size[prev] + 1 >= current_best_size:
            current_best_size = size[prev] + 1

    size[idx] = current_best_size

    if current_best_size > best_size:
        best_size = current_best_size

print(f"Maximum pairs connected: {best_size}")
