import sys
from bisect import bisect_left
sys.stdin = open("11053.txt", 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
DP = [nums[0]]
for num in nums:
    if num > DP[-1]:
        DP.append(num)
    else:
        DP[bisect_left(DP, num)] = num
print(len(DP))
