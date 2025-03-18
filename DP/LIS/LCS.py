import sys

sys.stdin = open('9251.txt', 'r')
input = sys.stdin.readline
A, B = input(), input()
X, Y = len(A), len(B)
DP = [[0] * (X + 1) for _ in range(Y + 1)]
for y in range(Y):
    for x in range(X):
        if A[x] == B[y]:
            DP[y + 1][x + 1] = DP[y][x] + 1
        else:
            DP[y + 1][x + 1] = max(DP[y][x + 1], DP[y + 1][x])
print(DP[Y][X])
