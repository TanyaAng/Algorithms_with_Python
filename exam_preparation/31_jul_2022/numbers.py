def is_descending(array):
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            return False
    return True


def subset_sum(numbers, target, temp):
    if sum(temp) == target:
        if is_descending(temp):
            print(*temp, sep=' + ')
    if sum(temp) >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        temp.append(n)
        print(f"Pre-recursion :{temp}")
        subset_sum(numbers, target, temp)
        temp.pop()
        print(f"Post-recursion :{temp}")


target = int(input())
numbers = list(range(target, 0, -1))
subset_sum(numbers, target, [])
