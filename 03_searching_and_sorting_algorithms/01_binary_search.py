def binary_search(collection, target):
    left = 0
    right = len(collection) - 1
    while left <= right:
        mid_idx = (right + left) // 2
        mid_el = collection[mid_idx]
        if mid_el == target:
            return mid_idx
        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())
print(binary_search(numbers, target))
