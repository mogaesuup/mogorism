arr = 'ABC'
result = []


def subset(k, choice):
    N = len(arr)
    for i in range(1 << N):
        temp = []
        for j in range(N):
            if i & (1 << j):
                continue
            temp.append(arr[j])
        choice.append(temp)
    return choice


print(subset(0, []))
