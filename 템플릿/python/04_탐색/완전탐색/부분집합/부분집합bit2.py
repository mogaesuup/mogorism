arr = 'ABC'
result = []


def subset():
    N = len(arr)
    for i in range(1 << N):
        choice = []
        for j in range(N):
            if i & (1 << j):
                choice.append(arr[j])
        result.append(choice[::])


subset()
print(result)
