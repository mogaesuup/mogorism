import sys
from collections import deque
sys.stdin = open("./11408.txt", "r")
INF = sys.maxsize
input = sys.stdin.readline
X, Y = map(int, input().split())
S = X + Y
E = X + Y + 1
C = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
F = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
cost = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
graph = [[] for _ in range(X + Y + 2)]

for i in range(X):
    C[S][i] = 1
    graph[S].append(i)
    graph[i].append(S)

for i in range(Y):
    C[i + X][E] = 1
    graph[i + X].append(E)
    graph[E].append(i + X)


for i in range(X):
    temp = list(map(int, input().split()))
    jobs = [temp[i:i + 2] for i in range(1, len(temp), 2)]
    for job in jobs:
        j, c = job
        j -= 1
        C[i][j + X] = 1
        cost[i][j + X] = c
        cost[j + X][i] = -c
        graph[i].append(j + X)
        graph[j + X].append(i)

count = 0
total = 0
while True:
    Q = deque([S])
    parent = [-1] * (X + Y + 2)
    dist = [INF] * (X + Y + 2)
    dist[S] = 0
    inQ = [False] * (X + Y + 2)
    inQ[S] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
    if parent[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[parent[x]][x]-F[parent[x]][x])
        x = parent[x]
    x = E
    while x != S:
        total += flow * cost[parent[x]][x]
        F[parent[x]][x] += flow
        F[x][parent[x]] -= flow
        x = parent[x]
    count += 1
print(count)
print(total)