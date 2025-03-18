import sys
sys.stdin = open('./text/1298.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(float, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

cpx = lambda x: complex(x[0], x[1])
ccw = lambda a, b, c, d: ((b - a).conjugate() * (d - c)).imag
rcpx = lambda x: (int(x.real), int(x.imag))

def convex_hull(P):
    U = []
    L = []
    for p in P:
        while len(U) > 1 and ccw(U[-2], U[-1], U[-1], p) >= 0: 
            U.pop()
        while len(L) > 1 and ccw(L[-2], L[-1], L[-1], p) <= 0: 
            L.pop()
        U.append(p)
        L.append(p)
    P = U[:] + L[-2::-1]
    P += P
    return P

def calipers(P):
    N = len(P) // 2 - 1
    a = 0
    b = 1
    Max = 0
    while a < N:
        dist = abs(P[b] - P[a])
        if dist > Max: 
            Max = dist
            Max_P = (P[a], P[b])
        if ccw(P[a], P[a + 1], P[b], P[b + 1]) < 0: 
            b += 1
        else: 
            a += 1
    return Max_P

for T in range(Int()):
    N = Int()
    P = set(cpx(List()) for _ in range(N))
    P = sorted(P, key=lambda c: (c.real,c.imag))
    if len(P) == 1: 
        print(int(P[0].real), int(P[0].imag))
    else:
        P = convex_hull(P)
        Max_P = calipers(P)
        print(int(Max_P[0].real), int(Max_P[0].imag), int(Max_P[1].real), int(Max_P[1].imag))