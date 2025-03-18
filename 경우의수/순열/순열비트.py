from itertools import permutations

r = 2
arr = ['A', 'B', 'C', 'D', 'E']
result = []

def perm(k, choice, used):
    if k == r:
        result.append(choice[::])
        return
    for i in range(len(arr)):
        if used & (1 << i):
            continue
        choice.append(arr[i])
        perm(k+1, choice, used | (1 << i))
        choice.pop()

perm(0, [], 0)
print(result)
print(list(permutations(arr, r)))
