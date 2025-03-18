import sys
sys.stdin = open('10868.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
tree = [0] * N + [int(input()) for _ in range(N)]
for i in reversed(range(1, N)):
    tree[i] = min(tree[2 * i], tree[2 * i ^ 1])


def query(l, r):
    res = sys.maxsize
    while l <= r:
        if l % 2:
            res = min(res, tree[l])
            l += 1
        if not (r % 2):
            res = min(res, tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    return res


for _ in range(M):
    a, b = map(int, input().split())
    a += N - 1
    b += N - 1
    print(query(a, b))
