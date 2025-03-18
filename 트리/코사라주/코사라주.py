import sys
sys.stdin = open("2150.txt", "r")
V, E = map(int, input().split())
visited = [False] * (V + 1)
graph = [[] for i in range(V + 1)]  # 빈 그래프 생성

# 주어진 간선에 따라 그래프 채워넣기
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
# dfs 재귀 함수


def dfs(v, visited, stack):
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            stack.append(w)
            dfs(w, visited, stack)
    stack.append(v)  # 탐색을 마친 노드 stack에 저장.

# 역방향 그래프 생성


def reverseDfs(v, visited, stack):
    visited[v] = 1
    stack.append(v)
    for w in reverse_graph[v]:
        if visited[w] == 0:
            reverseDfs(w, visited, stack)


# 코사라주 알고리즘
stack = []

for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack)  # stack에 탐색을 마친 정점 순으로 저장

reverse_graph = [[] for i in range(V+1)]
for i in range(1, V+1):
    for j in graph[i]:
        reverse_graph[j].append(i)

visited = [0] * (V+1)  # visited 초기화
results = []  # ssc를 담을 result 생성

while stack:
    scc = []
    node = stack.pop()  # stack에서 scc의 source 추출
    if visited[node] == 0:
        # dfs를 진행하면서, scc의 source부터 탐색을 진행한다. 탐색한 정점은 scc에 저장
        reverseDfs(node, visited, scc)
        results.append(sorted(scc) + [-1])  # 재귀가 끝난 정점이 ssc의 sink
print(results)
