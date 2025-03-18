def LPS(pat):
    lps = [0] * len(pat)
    t = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[t]:
            t += 1
            lps[i] = t
            i += 1
        else:
            if t != 0:
                t = lps[t-1]
            else:
                lps[i] = 0
                i += 1
    return pat, lps


pat = 'AABXAABA'
print(LPS(pat))
