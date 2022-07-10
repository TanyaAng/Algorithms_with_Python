# def find_super_set(collection):
#     if collection == []:
#         return [[]]
#     x = find_super_set(collection[1:])
#     return x + [[collection[0]] + y for y in x]

def is_unique_elements(subset):
    if len(subset) == len(set(subset)):
        return True
    return False


def find_super_set(idx, collection, subset):
    if is_unique_elements(subset):
        print(*subset)
    for i in range(idx, len(collection)):
        subset.append(collection[i])
        find_super_set(idx + 1, collection, subset)
        subset.pop()
    return


class py_solution:
    def sub_sets(self, subset):
        return sorted(self.subsetsRecur([], subset), key=lambda a: (len(a)))

    def subsetsRecur(self, current, subset):
        if subset:
            item_1=self.subsetsRecur(current, subset[1:])
            item_2=self.subsetsRecur(current + [subset[0]], subset[1:])
            return item_1+item_2
        return [current]


collection = sorted([int(x) for x in input().split(', ')])
print(py_solution().sub_sets(collection))
