from bisect import bisect_left
target = 4
nums =[1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
lo, hi = -1, len(nums) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if nums[mid] < target:
        lo = mid
    else:
        hi = mid
print(lo)
print(bisect_left(nums, 4))
