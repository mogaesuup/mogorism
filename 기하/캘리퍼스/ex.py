import sys
sys.stdin = open("1708.txt", "r")
input = sys.stdin.readline
N = int(input())
point = [list(map(int, input().split())) for i in range(N)]

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

U = []
L = []
point.sort()
for p in point:
    while len(U) >= 2 and ccw(U[-2], U[-1], p) <= 0:
        U.pop()
    while len(L) >= 2 and ccw(L[-2], L[-1], p) >= 0:
        L.pop()
    U.append(p)
    L.append(p)
print(len(U) + len(L) - 2)
