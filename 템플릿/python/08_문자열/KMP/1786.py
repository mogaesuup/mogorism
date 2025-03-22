import sys
sys.stdin = open("1786.txt", "r")
input = sys.stdin.readline

S = input()
P = input()
M = len(P)
N = len(S)
pi = [0] * M
pi[0] = 0
j = 0
for i in range(1, M):
    while j > 0 and P[i] != P[j]:
        j = pi[j - 1]
    if P[i] == P[j]:
        pi[i] = j + 1
        j += 1
    else:
        pi[i] = 0

j = 0
result = []
for i in range(N):
    while j > 0 and S[i] != P[j]:
        j = pi[j - 1]
    if S[i] == P[j]:
        if j == M - 1:
            result.append(i - (M - 1) + 1)
            j = pi[j]
        else:
            j += 1
print(len(result))
print(*result)
