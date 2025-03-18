def quicksort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[-1]
    before, after = [], []
    for num in nums[:-1]:
        if num < pivot:
            before.append(num)
        else:
            after.append(num)
    return quicksort(before) + [pivot] + quicksort(after)


print(quicksort([3, 1, 2, 4, 5]))
