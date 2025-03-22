import sys
sys.stdin = open("서로소집합.txt", 'r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v+1):
    print(find(parent, i), end=" ")
print()

print("부모 테이블: ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")
