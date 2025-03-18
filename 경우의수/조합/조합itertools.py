from itertools import combinations

#  조합 itertools
words = ['A', 'B', 'C', 'D', 'E']
comb = list(combinations(words, 2))
print(comb)

# 조합

r = 2
result = []


def comb(k, start, choice):
    if k == r:
        result.append(choice[::])
        return
    for i in range(start, len(words)):
        choice.append(words[i])
        comb(k + 1, i + 1, choice)
        choice.pop()


comb(0, 0, [])
print(result)
