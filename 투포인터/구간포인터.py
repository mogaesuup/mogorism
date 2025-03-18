import sys
sys.stdin = open('./test/14246.txt', 'r')
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
k = int(input())
j = sums = count = 0
for i in range(n):
    while sums <= k and j < n:
        sums += nums[j]
        j += 1
    if sums > k:
        count += n - j + 1
    sums -= nums[i]
print(count)