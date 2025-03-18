r = 2
arr = ['A', 'B', 'C', 'D', 'E']
result = []

def perm(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            # 다름(i만 제외한 배열 탐색 arr[:i] + arr[i+1:])
            for next in perm(arr[:i] + arr[i + 1 :], r - 1):
                yield [arr[i]] + next

for i in perm(arr, r):
    result.append(i)
    
print(result)
