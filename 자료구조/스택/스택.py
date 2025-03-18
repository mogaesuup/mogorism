class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def __str__(self):
        return "item : " + str(self.item) + "\n" + "next : " + str(self.next)


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        print(self.last.next)
        self.last = self.last.next
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    stack.pop()
