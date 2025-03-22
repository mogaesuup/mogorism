import sys
sys.stdin = open("2150.txt", "r")
V, E = map(int, input().split())
visited = [False] * (V + 1)
graph = [[] for i in range(V + 1)]  
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(v, visited, S):
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            S.append(w)
            dfs(w, visited, S)
    S.append(v) 

def reverseDfs(v, visited, S):
    visited[v] = 1
    S.append(v)
    for w in reverse_graph[v]:
        if visited[w] == 0:
            reverseDfs(w, visited, S)


# 코사라주 알고리즘
S = []

for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, S) 
reverse_graph = [[] for i in range(V+1)]
for i in range(1, V+1):
    for j in graph[i]:
        reverse_graph[j].append(i)

visited = [0] * (V + 1)
results = []
while S:
    scc = []
    node = S.pop() 
    if visited[node] == 0:
        reverseDfs(node, visited, scc)
        results.append(sorted(scc) + [-1]) 
print(results)
