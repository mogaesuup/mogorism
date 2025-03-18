import sys
from bisect import bisect_left, bisect_right

# 1 2 3 4 4 4 5 6 7 8
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
print(bisect_left(nums, 4))
print(bisect_right(nums, 4))
