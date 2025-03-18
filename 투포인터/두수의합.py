import sys
sys.stdin = open('./test/3273.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
result = 0
l, r = 0, N - 1
while l < r:
    if nums[l] + nums[r] >= M:
        if nums[l] + nums[r] == M:
            result += 1
        r -= 1
    if nums[l] + nums[r] < M:
        l += 1
print(result)
