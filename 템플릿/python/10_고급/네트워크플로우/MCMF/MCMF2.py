import sys
from collections import deque
sys.stdin = open("./11408.txt", "r")
INF = sys.maxsize
input = sys.stdin.readline
X, Y = map(int, input().split())
S = X + Y
E = X + Y + 1
N = X + Y + 2
C = [[0] * N for _ in range(N)]
F = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
graph = [[] for _ in range(N)]
count = 0
total = [0]
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

def SPFA():
    Q = deque([S])
    dist = [INF] * N
    inQ = [False] * N
    dist[S] = 0
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

def find(v, f):
    if v == S:
        return f
    u = parent[v]
    return find(u, min(f, C[u][v] - F[u][v]))

def flow(v, f):
    if v == S:return 
    u = parent[v]
    total[0] += f * cost[u][v]
    F[u][v] += f
    F[v][u] -= f
    flow(u, f)

while True:
    parent = [0] * N
    SPFA()
    if not parent[E]:break
    f = find(E, INF)
    flow(E, f)
    count += 1
print(count)
print(total[0])