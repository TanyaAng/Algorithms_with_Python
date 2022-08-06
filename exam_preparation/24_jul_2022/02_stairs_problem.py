def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


stairs = int(input())
print(fibonacci(stairs + 1))