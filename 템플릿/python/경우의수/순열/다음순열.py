import sys
sys.stdin = open('10972.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))


def next_permutation(nums):
    N = len(nums)
    i, j = N - 1, N - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        return [-1]
    while nums[j] <= nums[i-1]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]
    k = N - 1
    while i < k:
        nums[i], nums[k] = nums[k], nums[i]
        i += 1
        k -= 1
    return nums


print(*next_permutation(nums))
