import sys
sys.stdin = open("1708.txt", "r")
input = sys.stdin.readline


def C(t): return complex(t[0], t[1])


def F(a, b, c): return ((b-a).conjugate()*(c-b)).imag


N = int(input())
L = [C(list(map(int, input().split()))) for _ in range(N)]
L = sorted(L, key=lambda c: (c.real, c.imag))
P = []
Q = []
for p in L:
    while len(P) >= 2 and F(P[-2], P[-1], p) >= 0:
        P.pop()
    while len(Q) >= 2 and F(Q[-2], Q[-1], p) <= 0:
        Q.pop()
    P.append(p)
    Q.append(p)
print(len(P)+len(Q)-2)
