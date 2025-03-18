import sys
from collections import deque
from pprint import pprint
from heapq import heappop, heappush
sys.stdin = open('1922.txt', 'rt')
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

Q = []
visited[1] = True
result = 0
cnt = 1
for a in graph[1]:
    heappush(Q, a)
while Q:
    cost, u = heappop(Q)
    if not visited[u]:
        visited[u] = True
        cnt += 1
        result += cost
        for v in graph[u]:
            heappush(Q, v)
    if cnt == V:
        break
print(result)
