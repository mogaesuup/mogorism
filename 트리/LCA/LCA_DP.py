import sys
from collections import deque
from math import log2
sys.stdin = open("11438.txt", "r")
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0] * (N+1)
parent = [0] * (N+1)

logN = int(log2(N)) + 1
DP = [[0] * logN for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 전처리 BFS로 깊이와 부모 노드 구함
check = [False] * (N + 1)
Q = deque([1])
check[1] = True
while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not check[v]:
            check[v] = True
            depth[v] = depth[u] + 1
            parent[v] = u
            Q.append(v)
print(parent)
print(depth)
for i in range(N+1):
    DP[i][0] = parent[i]

for j in range(1, logN):
    for i in range(1, N+1):
        # i의 2 * j 번째 조상
        DP[i][j] = DP[DP[i][j-1]][j-1]
print(DP)


def LCA(u, v):
    # depth 기준으로 정리
    if depth[u] < depth[v]:
        u, v = v, u
    # depth 큰 것만 위로 올리기
    for i in range(logN - 1, -1, -1):
        if depth[u] - depth[v] >= (1 << i):
            u = DP[u][i]
    # 같으면 그대로 리턴
    if u == v:
        return v
    # 다르면 같기 직전까지 계속 위로 올림
    for i in range(logN - 1, -1, -1):
        if DP[u][i] != DP[v][i]:
            u = DP[u][i]
            v = DP[v][i]
    # 올린 것 바로 위의 조상
    return DP[u][0]


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
