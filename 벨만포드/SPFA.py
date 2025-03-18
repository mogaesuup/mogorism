import sys
from collections import deque
sys.stdin = open("11657.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
Y, X = map(int, input().split())
graph = [[] for _ in range(Y+1)]
for _ in range(X):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

def SPFA():
    dist = [INF] * (Y+1)
    inQ = [False] * (Y+1)
    count = [0] * (Y+1)
    dist[1] = 0
    Q = deque([1])
    inQ[1] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for cost, v in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
                    count[v] += 1
                    if count[v] >= Y:
                        return [-1]
    if Y == 1:
        return [dist[1]]
    else:
        return [-1 if x == INF else x for x in dist[2:]]


results = SPFA()
for result in results:
    print(result)
