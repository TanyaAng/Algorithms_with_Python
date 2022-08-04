# def recursive_power_set(numbers):
#     if len(numbers) == 0:
#         return []
#     base = recursive_power_set(numbers[:-1])
#     operator = numbers.pop()
#     result = base + [(b + operator) for b in base]
#     return result


def iterative_power_set(numbers):
    result = [[]]
    for l in range(len(numbers)):
        for k in range(len(result)):
            result.append(result[k] + numbers[l:l + 1])
    return result


numbers = [int(x) for x in input().split(', ')]
result = iterative_power_set(numbers)[1:]

print()
for set in sorted(result, key=lambda x: (len(x), x[0], x[-1])):
    print(*set, sep=' ')
