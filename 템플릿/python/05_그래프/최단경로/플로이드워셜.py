import sys
sys.stdin = open("플로이드워셜.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c, = map(int, input().split())
    graph[a][b] = c

for y in range(1, N+1):
    for x in range(1, N+1):
        if y == x:
            graph[y][x] = 0

for z in range(1, N+1):
    for y in range(1, N+1):
        for x in range(1, N+1):
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])

for y in range(1, N+1):
    print(graph[y][1:])
