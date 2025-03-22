import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("2213.txt", "r")
input = sys.stdin.readline
N = int(input())
DP = [[0, 0] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
A = [0] + list(map(int, input().split()))
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
result = []


def dfs(prev, u):
    DP[u][1] = A[u]
    for v in tree[u]:
        if prev != v:
            dfs(u, v)
            DP[u][0] += max(DP[v][0], DP[v][1])
            DP[u][1] += DP[v][0]


def trace(prev, u, k):
    if k:
        result.append(u)
        for v in tree[u]:
            if prev != v:
                trace(u, v, 0)
    else:
        for v in tree[u]:
            if prev != v:
                if DP[v][0] < DP[v][1]:
                    trace(u, v, 1)
                else:
                    trace(u, v, 0)


dfs(0, 1)
if DP[1][0] < DP[1][1]:
    trace(0, 1, 1)
else:
    trace(0, 1, 0)

print(max(DP[1]))
result.sort()
for i in result:
    print(i, end=' ')
