def LPS(pat):
    lps = [0] * (len(pat) + 1)
    t = 1
    p = 0
    while t != len(pat):
        if pat[t] == pat[p]:
            t += 1
            p += 1
            lps[t] = p
        elif p == 0:
            t += 1
            lps[t] = p
        else:
            p = lps[p]
    return lps


def kmp(txt, pat):
    lps = LPS(pat)
    P = len(pat)
    j = 0
    result = []
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = lps[j-1]
        if txt[i] == pat[j]:
            if j == P - 1:
                result.append(i - P + 1)
                j = lps[j]
            else:
                j += 1
    return result


txt = 'ABXABABYABCDE'
pat = 'BBYXAB'
print(kmp(txt, pat))
