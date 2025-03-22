import sys
sys.stdin = open("11657.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
Y, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(X)]


def bellman_ford():
    # 구현부
    dist = [INF] * (Y + 1)
    dist[1] = 0
    # Y회 순회
    for y in range(Y):
        # 실제 작동부
        for x in range(X):
            u, v, cost = edges[x]
            if dist[u] != INF and dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                # y-1이상에서 dist가 바뀐다면 사이클 있음
                if y == Y - 1:
                    return [-1]
    # 구현부
    if Y == 1:
        return [dist[0]]
    return [-1 if x == INF else x for x in dist[2:]]


results = bellman_ford()
for result in results:
    print(result)
