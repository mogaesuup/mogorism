from pprint import pprint
import sys
sys.stdin = open("플로이드워셜.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

# 입력부분
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c, = map(int, input().split())
    graph[a][b] = c

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for y in range(1, N+1):
    for x in range(1, N+1):
        if y == x:
            graph[y][x] = 0

# 플로이드 워셜 알고리즘을 수행
for z in range(1, N+1):
    for y in range(1, N+1):
        for x in range(1, N+1):
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])

# 수행한 결과를 출력
for y in range(1, N+1):
    print(graph[y][1:])
