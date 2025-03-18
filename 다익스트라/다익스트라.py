from heapq import heappop, heappush
import sys
sys.stdin = open("다익스트라.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def dijkstra(start):
    dist = [INF] * (n+1)
    Q = [(0, start)]
    dist[start] = 0
    while Q:
        cost, u = heappop(Q)
        if dist[u] < cost:
            continue
        for w, v in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(Q, (dist[v], v))
    return dist


dist = dijkstra(start)
for i in range(1, n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
