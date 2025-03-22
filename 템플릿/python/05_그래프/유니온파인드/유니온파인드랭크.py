import sys
sys.stdin = open("서로소집합.txt", 'r')

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
rank = [0 for _ in range(v+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] = rank[b] + 1


for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v+1):
    print(find(i), end=" ")
print()

print("부모 테이블: ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")
