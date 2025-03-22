import sys
sys.stdin = open('./text/13264.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Int():return int(input().strip())
def Str():return input().strip()

S = Str()
N = len(S)
SA = [i for i in range(N)] 
ISA = [ord(S[i]) for i in range(N)] + [-1]
_ISA = [0] * N + [-1]
t = 1
while t < N:
    SA.sort(key = lambda x: (ISA[x], ISA[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i], SA[i - 1]
        if ISA[a] != ISA[b] or ISA[min(a + t, N)] != ISA[min(b + t, N)]:
            _ISA[a] = _ISA[b] + 1
        else:
            _ISA[a] = _ISA[b]
    t *= 2
    ISA = _ISA[:]

for sa in SA:
    print(sa)