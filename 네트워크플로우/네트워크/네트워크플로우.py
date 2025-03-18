# network flow
from sys import *
from collections import deque
from pprint import *
stdin = open('네트워크플로우.txt', 'r')
input = stdin.readline
n, m = map(int, input().split())
MAX = n+2
adj = [[]for _ in range(MAX)]
c = [[0] * MAX for _ in range(MAX)]
f = [[0] * MAX for _ in range(MAX)]
s, e = 0, 1
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)
    c[u][v] = 1
total = 0
while True:
    q = deque()
    q.append(s)
    visited = [-1] * MAX
    visited[s] = s
    while q and visited[e] == -1:
        u = q.popleft()
        for v in adj[u]:
            if c[u][v]-f[u][v] > 0 and visited[v] == -1:
                visited[v] = u
                q.append(v)
    if visited[e] == -1:
        print(total)
        break
    v = e
    while v != s:
        u = visited[v]
        f[u][v] += 1
        f[v][u] -= 1
        v = u
    total += 1
