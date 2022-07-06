def recursion_reverse_array(numbers):
    if len(numbers)==0:
        return ''
    return f"{numbers.pop()} {recursion_reverse_array(numbers)}"


numbers = input().split()
print(recursion_reverse_array(numbers))
