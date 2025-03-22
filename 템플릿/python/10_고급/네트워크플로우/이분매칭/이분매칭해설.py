import sys
sys.setrecursionlimit(100 * 100)
sys.stdin = open('./test/2188.txt', 'r')
input = sys.stdin.readline
def dfs(n):
    N[n] = False
    for m in g[n]:
        if not M[m] or (N[M[m]] and dfs(M[m])):
            N[n] = True
            M[m] = n
            return True
    return False
n, m = map(int, input().split())
g = {}
for i in range(1, n + 1):
    g[i] = list(map(int, input().split()))[1:]
N = [True for _ in range(n + 1)]
M = [False for _ in range(m + 1)]
result = 0
for i in range(1, n + 1):
    if dfs(i):
        result += 1
print(result)