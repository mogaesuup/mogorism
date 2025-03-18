import sys
from heapq import heappop, heappush
sys.stdin = open("1922.txt", 'r')

V = int(input())
E = int(input())
parent = [i for i in range(V+1)]

heap = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    heappush(heap, (cost, a, b))
result = 0


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


while heap:
    cost, a, b = heappop(heap)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(result)
