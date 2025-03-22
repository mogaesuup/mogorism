# Binary Search Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = self.parent = None

    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insertKey(self.root, key)
        return self.root is not None

    def insertKey(self, node, key):
        if node is None:
            node = Node(key)
        else:
            if node.key >= key:
                node.left = self.insertKey(node.left, key)
            else:
                node.right = self.insertKey(node.right, key)
        return node

    def find(self, key):
        return self.findKey(self.root, key)

    def findKey(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self.findKey(node.left, key)
        else:
            return self.findKey(node.right, key)

    def delete(self, key):
        self.root, deleted = self.deleteKey(self.root, key)
        return deleted

    def deleteKey(self, node, key):
        if node is None:
            return None, False

        deleted = False

        if key == node.key:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left

                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node, deleted = None, False
        elif key < node.key:
            node.left, deleted = self.deleteKey(node.left, key)
        else:
            node.right, deleted = self.deleteKey(node.right, key)

        return node, deleted

    def inorder(self):
        self.printOrder(self.root)
        print()

    def printOrder(self, node):
        if node is None:
            return
        self.printOrder(node.left)
        print(node, end=" ")
        self.printOrder(node.right)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

bst.inorder()

# Find
print(bst.find(15))  # True
print(bst.find(17))  # False

# Delete
print(bst.delete(55))  # True
print(bst.delete(14))  # True
print(bst.delete(11))  # False
bst.inorder()
