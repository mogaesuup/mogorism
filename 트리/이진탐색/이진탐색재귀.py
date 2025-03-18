def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾는 값이 가운데
    if array[mid] == target:
        return mid
    # 찾는 값이 가운데보다 작음
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 찾는 값이 가운데보다 큼
    else:
        return binary_search(array, target, mid+1, end)


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
n = 10
target = 7
result = binary_search(array, target, 0, n-1)
print(result+1)
