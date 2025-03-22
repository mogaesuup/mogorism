def heap_sort(arr):
    for i in range(1, len(arr)):
        c = i
        while c != 0:
            r = (c-1)//2
            if arr[r] < arr[c]:
                arr[r], arr[c] = arr[c], arr[r]
            c = r

    for j in range(len(arr)-1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        r = 0
        c = 1
        while c < j:
            c = 2 * r + 1
            if c < j - 1 and arr[c] < arr[c+1]:
                c += 1
            if c < j and arr[r] < arr[c]:
                arr[r], arr[c] = arr[c], arr[r]
            r = c
    return arr


print(heap_sort([3, 2, 4, 5, 1]))
