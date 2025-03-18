import sys
from bisect import bisect_left, bisect_right
sys.stdin = open('이진탐색.txt', 'r')

# 1 2 3 4 4 4 5 6 7 8
N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(bisect_left(nums, 4))
print(bisect_right(nums, 4))
