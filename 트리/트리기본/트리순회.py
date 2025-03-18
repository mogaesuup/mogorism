import sys
sys.stdin = open('트리순회.txt', 'r')


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


input = sys.stdin.readline
N = int(input())
tree = {}
A = ord('A')
for _ in range(N):
    a, b, c = map(str, input().split())
    a = ord(a) - A
    left = -1 if b == '.' else ord(b) - A
    right = -1 if c == '.' else ord(c) - A
    tree[a] = Node(left, right)


def preorder(x):
    if x == -1:
        return
    print(chr(x + A), end='')
    preorder(tree[x].left)
    preorder(tree[x].right)


def postorder(x):
    if x == -1:
        return
    postorder(tree[x].left)
    postorder(tree[x].right)
    print(chr(x + A), end='')


def inorder(x):
    if x == -1:
        return
    inorder(tree[x].left)
    print(chr(x + A), end='')
    inorder(tree[x].right)


preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
