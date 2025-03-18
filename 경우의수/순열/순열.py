from pprint import pprint

def PERM(arr, r):
    result = []
    used = [0 for _ in range(len(arr))]

    def perm(k, chosen, used):
        if k == r:
            result.append(chosen[::])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            chosen.append(arr[i])
            used[i] = 1
            perm(k+1, chosen, used)
            used[i] = 0
            chosen.pop()
    perm(0, [], used)
    return result


result = PERM('ABCDE', 3)
pprint(result)
pprint(str(len(result)) + "개")
