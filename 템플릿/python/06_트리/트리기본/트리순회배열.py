import sys
sys.stdin = open('트리순회.txt', 'r')
input = sys.stdin.readline


def num(x):
    return ord(x)-64


def word(x):
    return chr(x+64)


def preorder(x):
    if x == -1:
        return
    print(word(x), end="")
    preorder(tree[x][0])
    preorder(tree[x][1])


def inorder(x):
    if x == -1:
        return
    inorder(tree[x][0])
    print(word(x), end="")
    inorder(tree[x][1])


def postorder(x):
    if x == -1:
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(word(x), end="")


N = int(input())
tree = [[-1, -1] for _ in range(N+1)]
for _ in range(N):
    a, b, c = map(str, input().split())
    tree[num(a)][0] = -1 if b == '.' else num(b)
    tree[num(a)][1] = -1 if c == '.' else num(c)
preorder(1)
print()
inorder(1)
print()
postorder(1)
