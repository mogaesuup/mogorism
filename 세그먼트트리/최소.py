import sys
from math import ceil, log2

# 10868
sys.stdin = open('10868.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
size = (1 << (ceil(log2(N))+1))

board = [int(input()) for _ in range(N)]
tree = [0] * (size)


def init(x, s, e):
    if s == e:
        tree[x] = board[e]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = min(init(2 * x, s, mid), init(2 * x + 1, mid + 1, e))
    return tree[x]


def query(x, s, e, S, E):
    if S > e or s > E:
        return sys.maxsize
    if s >= S and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return min(query(2 * x, s, mid, S, E), query(2 * x + 1, mid + 1, e, S, E))


init(1, 0, N-1)

for _ in range(M):
    s, e = map(int, input().split())
    print(query(1, 0, N-1, s-1, e-1))
