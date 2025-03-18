import sys
# 10868
sys.stdin = open('세그먼트트리.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)


def init(x, start, end):
    if start == end:
        tree[x] = board[end]
    else:
        mid = (start + end) // 2
        init(2 * x, start, mid)
        init(2 * x + 1, mid + 1, end)
        tree[x] = min(tree[2 * x], tree[2 * x + 1])


init(1, 0, N-1)


def query(x, start, end, S, E):
    if end < S or start > E:
        return -1
    if start >= S and end <= E:
        return tree[x]
    mid = (start + end) // 2
    left = query(2 * x, start, mid, S, E)
    right = query(2 * x + 1, mid + 1, end, S, E)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return min(left, right)


for _ in range(M):
    start, end = map(int, input().split())
    print(query(1, 0, N-1, start-1, end-1))
