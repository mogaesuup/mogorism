# network flow
from sys import *
from collections import deque
from pprint import *
stdin = open('네트워크플로우.txt', 'r')
input = stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+2)]
C = [[0] * (N+2) for _ in range(N+2)]
F = [[0] * (N+2) for _ in range(N+2)]
start, end = 0, 1
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
    C[u][v] = 1
total = 0
while True:
    Q = deque()
    Q.append(start)
    visited = [-1] * (N+2)
    visited[start] = start
    while Q and visited[end] == -1:
        u = Q.popleft()
        for v in graph[u]:
            if C[u][v] - F[u][v] > 0 and visited[v] == -1:
                visited[v] = u
                Q.append(v)
    if visited[end] == -1:
        print(total)
        break
    v = end
    while v != start:
        u = visited[v]
        F[u][v] += 1
        F[v][u] -= 1
        v = u
    total += 1
