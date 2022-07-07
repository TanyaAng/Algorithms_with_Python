# VARIANT I
def reverse_array(idx,elements):
    if idx==len(elements)//2:
        return
    swap_idx=len(elements)-1-idx
    elements[idx],elements[swap_idx]=elements[swap_idx],elements[idx]
    reverse_array(idx+1, elements)

# VARIANT II
def recursion_reverse_array(numbers):
    if len(numbers)==0:
        return ''
    return f"{numbers.pop()} {recursion_reverse_array(numbers)}"


numbers = input().split()
reverse_array(0, numbers)
print(' '.join(numbers))

# print(recursion_reverse_array(numbers))
