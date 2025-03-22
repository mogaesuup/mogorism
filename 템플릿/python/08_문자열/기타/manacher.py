word = "ABCBA"
word = "@" + "@".join(word) + "@"
print(word)

def manacher(word):
    N = len(word)
    p = [0] * N
    r = c = -1
    Max = 0
    for i in range(1, N):
        if i <= r:
            p[i] = min(r - i, p[2 * c - i])
        else:   
            p[i] = 0

        R = p[i] + 1
        while i + R < N and word[i - R] == word[i + R]:
            p[i] += 1
            R += 1

        if r < i + p[i]:
            r = i + p[i]
            c = i
        Max = max(p[i], Max)
    return Max

print(manacher(word))