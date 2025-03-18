import sys
sys.stdin = open("9655.txt", "r")
input = sys.stdin.readline
N = int(input())
DP = [True] * (N+1)
DP[0] = True
for i in range(1, N+1):
    DP[i] = True
    if i - 1 >= 0 and DP[i-1]:
        DP[i] = False
    if i - 3 >= 0 and DP[i-3]:
        DP[i] = False
if DP[N]:
    print("SK")
else:
    print("CY")
