import sys
sys.stdin = open("./test/1717.txt", 'r')

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def F(x):
    if x != parent[x]:
        parent[x] = F(parent[x])
    return  parent[x]
        
def U(a, b):
    parent[max(F(a), F(b))] = min(F(a), F(b))


for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        U(b, c)
    else:
        if F(b) == F(c):
            print('YES')
        else:
            print('NO')
