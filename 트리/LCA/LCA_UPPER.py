import sys
from math import log2
sys.setrecursionlimit(200000)
sys.stdin = open("upper.txt", "r")
input = sys.stdin.readline

N = int(input())
log = int(log2(N)+1)
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

P = [[0] * (log+1) for i in range(N+1)]
tin = [0 for _ in range(N+1)]
tout = [0 for _ in range(N+1)]
timer = 0


def dfs(u, parent):
    global timer
    timer += 1
    tin[u] = timer
    P[u][0] = parent
    for i in range(1, log+1):
        P[u][i] = P[P[u][i-1]][i-1]
    for v in tree[u]:
        if v != parent:
            dfs(v, u)
    timer += 1
    tout[u] = timer


dfs(1, 1)


def upper(u, v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]


def LCA(u, v):
    if upper(u, v):
        return u
    if upper(v, u):
        return v
    for i in range(log, -1, -1):
        if not upper(P[u][i], v):
            u = P[u][i]
    return P[u][0]


M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
