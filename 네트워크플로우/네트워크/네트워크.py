import sys
sys.stdin = open('네트워크.txt', 'r')


def DFS(start):
    if(visitedN[start] != -1):
        return 0
    visitedN[start] = 1
    for i in range(M):
        if(visited[i] == start or adj[start][i+N] != 1):
            continue
        if(visited[i] == -1 or DFS(visited[i]) == 1):
            visited[i] = start
            return 1
    return 0


N, M = input().split()
N, M = int(N), int(M)

cowArray = [[]] * N
for i in range(N):
    cowArray[i] = [int(k) for k in input().split()]
totalVertex = M + N
adj = [[0]*totalVertex for i in range(totalVertex)]

visited = [-1] * M
total = 0

for i, j in enumerate(cowArray):
    for k in range(j[0]):
        adj[i][j[k+1]+N - 1] = 1

for i in range(N):
    visitedN = [-1] * N
    if(DFS(i) == 1):
        total += 1

print(total)
