graph = [
    [],
    [2, 3, 8],  # 1
    [1, 7],     # 2
    [1, 4, 5],  # 3
    [3, 5],     # 4
    [3, 4],     # 5
    [7],        # 6
    [2, 6, 8],  # 7
    [1, 7]      # 8
]


def DFS(v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            DFS(i, visited)


visited = [False] * 9
DFS(1, visited)
