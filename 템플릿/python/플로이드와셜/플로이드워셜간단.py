import sys
sys.stdin = open("플로이드워셜.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF]*(N) for _ in range(N)]
for _ in range(M):
    a, b, c, = map(int, input().split())
    graph[a-1][b-1] = c

for y in range(N):
    for x in range(N):
        if y == x:
            graph[y][x] = 0
for z in range(N):
    for y in range(N):
        for x in range(N):
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])

for g in graph:
    print(*g)
