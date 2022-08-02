n = int(input())
k = int(input())


# VARIANT I
def calc_binom(n, k, memo):
    key = f'{n} {k}'
    if key in memo:
        return memo[key]
    if n == 0 or k == 0 or n == k:
        return 1
    result = calc_binom(n - 1, k - 1, memo) + calc_binom(n - 1, k, memo)
    memo[key] = result
    return result

print(calc_binom(n, k, {}))

# VARIANT II
# def factorial(n, memo):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         memo[0] = 1
#         return memo[0]
#     if n == 1:
#         memo[1] = 1
#         return memo[1]
#     result = n * factorial(n - 1, memo)
#     memo[n] = result
#     return result

# def find_binomial_coefficient(n, k):
#     memo = {}
#     return factorial(n, memo) / (factorial(k, memo) * factorial(n - k, memo))

# print(int(find_binomial_coefficient(n, k)))
