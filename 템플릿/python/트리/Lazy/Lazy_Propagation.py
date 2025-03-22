from math import ceil, log2
import sys
sys.stdin = open('10999.txt', 'r')

input = sys.stdin.readline
n, m, k = map(int, input().split())
h = ceil(log2(n))
board = [int(input()) for i in range(n)]
tree = [0] * (1 << (h+1))
lazy = [0] * (1 << (h+1))


def init(x, s, e):
    if s == e:
        tree[x] = board[s]
        return tree[x]
    mid = (s+e) // 2
    tree[x] = init(2 * x, s, mid) + init(2 * x + 1, mid + 1, e)
    return tree[x]


def propagate(x, s, e, diff):
    tree[x] += (e - s + 1) * diff
    if s != e:
        lazy[2 * x] += diff
        lazy[2 * x + 1] += diff


def lazy_update(x, s, e):
    if lazy[x] == 0:
        return
    propagate(x, s, e, lazy[x])
    lazy[x] = 0


def update(x, s, e, S, E, diff):
    lazy_update(x, s, e)
    if S > e or s > E:
        return
    if S <= s and e <= E:
        propagate(x, s, e, diff)
        return
    mid = (s + e)//2
    update(2 * x, s, mid, S, E, diff)
    update(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] + tree[2 * x + 1]


def sum(x, s, e, S, E):
    lazy_update(x, s, e)
    if S > e or E < s:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e)//2
    return sum(2 * x, s, mid, S, E) + sum(2 * x + 1, mid + 1, e, S, E)


init(1, 0, n-1)
for i in range(m+k):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        a, b, c, d = temp
        update(1, 0, n-1, b-1, c-1, d)
    else:
        a, b, c = temp
        print(sum(1, 0, n-1, b-1, c-1))
