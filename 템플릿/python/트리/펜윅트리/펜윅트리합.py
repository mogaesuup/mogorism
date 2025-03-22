import sys
sys.stdin = open('펜윅트리합.txt', 'r')

input = sys.stdin.readline
n, m, k = map(int, input().split())
tree = [0] * (n+1)


def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)


def sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s


board = [0]
for i in range(1, n+1):
    board.append(int(input()))
    update(i, board[i])
for i in range(0, m+k):
    q, a, b = map(int, input().split())
    if q == 1:
        update(a, b-board[a])
        board[a] = b
    if q == 2:
        print(sum(b) - sum(a-1))
