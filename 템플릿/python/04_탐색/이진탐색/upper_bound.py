from bisect import bisect_right
target = 4
nums =[1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
start, end = -1, len(nums)
while start + 1 < end:
    mid = (start + end) // 2
    if nums[mid] <= target:
        start = mid
    else:
        end = mid
print(end)
print(bisect_right(nums, 4))