p = 'abcdabcef'
s = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text
base = 256
mod = 127


def hash(S):
    result = 0
    for s in S:
        result = (result * base + ord(s)) % mod
    return result


def rabin_karp(p, s):
    hash_p = hash(p)
    m = len(p)
    n = len(s)
    if m <= n:
        hash_s = hash(s[0:m])
        first = 1
        for i in range(m-1):
            first = (first*base) % mod
        for i in range(n-m+1):
            if hash_s == hash_p:
                if s[i:i+m] == p:
                    result = 1
                    break
            if i+m < n:
                hash_s = hash_s - (ord(s[i])*first) % mod
                hash_s = (hash_s + mod) % mod
                hash_s = ((hash_s * base) % mod + ord(s[i+m])) % mod
    return result


print(rabin_karp(p, s))
