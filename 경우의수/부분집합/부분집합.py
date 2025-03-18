arr = 'ABC'
result = []


def subset(k, choice):
    if k == len(arr):
        result.append(choice[::])
        return
    choice.append(arr[k])
    subset(k+1, choice)   # 왼쪽
    choice.pop()
    subset(k+1, choice)   # 오른쪽


subset(0, [])
print(result)
