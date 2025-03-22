def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    L, M, H = [], [], []
    for num in arr:
        if num < pivot: L.append(num)
        elif num > pivot: H.append(num)
        else: M.append(num)
    return quick(L) + M + quick(H)

print(quick([3, 1, 4, 5, 2]))
