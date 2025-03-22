import sys
INF = sys.maxsize

for _ in range(int(input())):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    for _ in range(w):
        a, b, c = map(int, input().split())
        graph[a].append([b, -c])

    dist = [INF] * (n + 1)
    dist[1] = 0
    result = "NO"
    for it in range(n):
        for v in range(1, n+1):
            for nv, nw in graph[v]:
                if dist[nv] > dist[v] + nw:
                    dist[nv] = dist[v] + nw
                    if it == n-1:
                        result = "YES"
                        break
    print(result)
