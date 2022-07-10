import numpy as np

'''Not the appropriate solution'''
# def find_super_set(idx, collection, subset):
#     if is_unique_elements(subset):
#         print(*subset)
#     for i in range(idx, len(collection)):
#         subset.append(collection[i])
#         find_super_set(idx + 1, collection, subset)
#         subset.pop()
#     return

'''The same as class implementation'''
# def find_super_set(current, collection):
#     if collection:
#         item_1 = find_super_set(current, collection[1:])
#         item_2 = find_super_set(current + [collection[0]], collection[1:])
#         result = item_1 + item_2
#         return result
#     return [current]

'''Can not order by the requirments'''


# class py_solution:
#     def sub_sets(self, subset):
#         return sorted(self.__subsetsRecur([], subset), key=lambda a: (len(a)))
#
#     def __subsetsRecur(self, current, subset):
#         if subset:
#             item_1 = self.__subsetsRecur(current, subset[1:])
#             item_2 = self.__subsetsRecur(current + [subset[0]], subset[1:])
#             result = item_1 + item_2
#             return result
#         return [current]
#
#
# collection = sorted([int(x) for x in input().split(', ')])
# solution = py_solution()
# print(solution.sub_sets(collection))


def is_lexicographical_order(array):
    return sorted(array) == array


def is_unique_elements(subset):
    return len(subset) == len(set(subset))


def clear_vector(vector):
    return [item for item in vector if item != None]


def super_set(idx, collection, vector):
    if idx >= len(vector):
        if is_unique_elements(vector) and is_lexicographical_order(vector):
            print(*vector, sep=' ')
        return
    for i in range(len(collection)):
        if collection[i] in vector:
            continue
        vector[idx] = collection[i]
        cleared_vector = clear_vector(vector)
        if len(cleared_vector) < len(vector) and is_unique_elements(cleared_vector) and is_lexicographical_order(
                cleared_vector):
            print(*cleared_vector, sep=' ')
        super_set(idx + 1, collection, vector)
        vector[idx] = None


collection = sorted([int(x) for x in input().split(', ')])
vector = [None] * len(collection)
super_set(0, collection, vector)
