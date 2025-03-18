import sys
sys.setrecursionlimit(2000*2000)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if DP[n] != -1:
        return DP[n]
    DP[n] = fibonacci(n-1) + fibonacci(n-2)
    return DP[n]


n = 10
DP = [-1] * (n+1)
fibonacci(n)
print(DP[n])
