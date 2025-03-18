import sys
sys.stdin = open('펜윅트리.txt', 'r')
input = sys.stdin.readline
MAX = 1000000001


def update(i, x):
    while i <= n:
        tree[i] = min(tree[i], x)
        i += (i & -i)


def update2(i, x):
    while i > 0:
        tree2[i] = min(tree2[i], x)
        i -= (i & -i)


def query(a, b):
    v = MAX
    prev = a
    curr = prev + (prev & -prev)
    while curr <= b:
        v = min(v, tree2[prev])
        prev = curr
        curr = prev + (prev & -prev)
    v = min(v, arr[prev])
    prev = b
    curr = prev - (prev & -prev)
    while curr >= a:
        v = min(v, tree[prev])
        prev = curr
        curr = prev - (prev & -prev)
    return v


n, m = map(int, input().split())
arr = [0] * (n+1)
tree = [MAX] * (n+2)
tree2 = [MAX] * (n+2)
for i in range(1, n+1):
    arr[i] = int(input())
    update(i, arr[i])
    update2(i, arr[i])

for i in range(m):
    a, b = map(int, input().split())
    print(query(a, b))
