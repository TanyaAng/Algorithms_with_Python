n = int(input())
k = int(input())


def factorial(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 1
        return memo[0]
    if n == 1:
        memo[1] = 1
        return memo[1]
    result = n * factorial(n - 1, memo)
    memo[n] = result
    return result


def find_binomial_coefficient(n, k):
    memo = {}
    return factorial(n, memo) / (factorial(k, memo) * factorial(n - k, memo))


print(int(find_binomial_coefficient(n, k)))

