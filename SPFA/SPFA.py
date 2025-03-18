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
    dp = [INF] * (Y + 1)
    cycle = [0] * (Y + 1)
    dp[1] = 0
    inQ = [False] * (Y + 1)
    Q = deque([1])
    inQ[1] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for w, v in graph[u]:
            if dp[v] > dp[u] + w:
                dp[v] = dp[u] + w
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
                    cycle[v] += 1
                    if cycle[v] >= Y:
                        return [-1]
    if Y == 1:
        return [dp[1]]
    return list(map(lambda x: x if x != INF else -1, dp[2:]))


results = SPFA()
for result in results:
    print(result)
