import sys
sys.stdin = open("11053.txt", "r")

N = int(input())
nums = [0] + list(map(int, input().split()))
DP = [0] * (N + 1)
DP[1] = 1
for i in range(2, N + 1):
    for j in range(1, i):
        if nums[i] > nums[j]:
            DP[i] = max(DP[j], DP[i])
    DP[i] += 1
print(max(DP))
