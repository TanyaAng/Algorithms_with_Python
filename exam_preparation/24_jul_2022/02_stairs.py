# Recursive Fibonacci
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# stairs = int(input())
# print(fibonacci(stairs + 1))

# Iterative Fibonacci
stairs=int(input())
one, two = 1, 1
for i in range(stairs - 1):
    one, two = one + two, one
print(one)
