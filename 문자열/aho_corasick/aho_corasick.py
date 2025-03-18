# import sys
# sys.stdin = open('9250.txt', 'r')


# class Node:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.word = False

#     def __repr__(self):
#         return f'TrieNode({self.word}:{self.children.items()})'


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def add(self, word):
#         node = self.root
#         for char in word:
#             node = node.children[char]
#         node.word = True

#     # 단어 존재 여부 판별
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]


