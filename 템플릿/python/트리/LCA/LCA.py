from collections import deque
import sys
sys.stdin = open('LCA.txt', 'r')


def LCA(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    while depth[u] != depth[v]:
        u = parent[u]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u


N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0] * (N+1)
check = [False] * (N+1)
parent = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

check[1] = True
Q = deque([1])

while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not check[v]:
            depth[v] = depth[u] + 1
            check[v] = True
            parent[v] = u
            Q.append(v)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
