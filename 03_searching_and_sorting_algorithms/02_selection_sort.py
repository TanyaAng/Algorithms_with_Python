def selection_sort(array):
    for idx in range(len(array)):
        min_number = array[idx]
        min_idx = idx
        for next_idx in range(idx + 1, len(array)):
            next_number = array[next_idx]
            if next_number < min_number:
                min_number = next_number
                min_idx = next_idx
        array[idx], array[min_idx] = array[min_idx], array[idx]
    return array


array = [int(x) for x in input().split()]
print(*selection_sort(array), sep=' ')
