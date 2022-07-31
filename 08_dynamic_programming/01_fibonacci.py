n = int(input())


def calc_fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = calc_fib(n - 2, memo) + calc_fib(n - 1, memo)
    memo[n] = result
    return result


print(calc_fib(n, {}))
