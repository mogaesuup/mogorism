import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("2533.txt", "r")
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]
DP = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(prev, u):
    DP[u][0] = 0
    DP[u][1] = 1
    for v in tree[u]:
        if prev != v:
            dfs(u, v)
            DP[u][0] += DP[v][1]
            DP[u][1] += min(DP[v][0], DP[v][1])


dfs(0, 1)
print(min(DP[1][0], DP[1][1]))
