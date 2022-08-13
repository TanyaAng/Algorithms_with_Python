def is_ascending(array):
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            return False
    return True


def find_cost(sequence, cost_of_flasks):
    total_cost = 0
    for n in sequence:
        total_cost += cost_of_flasks[n - 1]
    return total_cost


def subset_sum(numbers, target, current, cost_of_flasks, result):
    if sum(current) == target:
        if is_ascending(current):
            total_cost = find_cost(current, cost_of_flasks)
            if total_cost not in result:
                result[total_cost] = []
                result[total_cost].extend(current)
    if sum(current) >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        current.append(n)
        subset_sum(numbers, target, current, cost_of_flasks, result)
        current.pop()


cost_of_flasks = [int(x) for x in input().split()]
target = int(input())
packages_of_flasks = list(range(1, len(cost_of_flasks) + 1))
result = {}

subset_sum(packages_of_flasks, target, [], cost_of_flasks, result)
# print(result)
min_sum = min(result.keys())
min_array = result[min_sum]
print(f"Cost: {min_sum}")
for n in min_array:
    print(f"{n} => {cost_of_flasks[n - 1]}")
