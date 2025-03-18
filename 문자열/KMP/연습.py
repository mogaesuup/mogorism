def LPS(pattern):
    N = len(pattern)
    results = [0] * N
    p = 0
    i = 1
    while i < N:
        if pattern[p] == pattern[i]:
            p += 1
            results[i] = p
            i += 1
        else:
            if p != 0:
                p = results[p - 1]
            else:
                results[i] = 0
                i += 1
    return results


print(LPS("AABCAAB"))
