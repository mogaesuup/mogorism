class Trie:
    head = {}

    def add(self, words):
        _head = self.head
        for word in words:
            if word not in _head:
                _head[word] = {}
            _head = _head[word]
        _head['*'] = True

    def search(self, words):
        _head = self.head
        for word in words:
            if word not in _head:
                return False
            _head = _head[word]
        if '*' in _head:
            return True
        else:
            return False


trie = Trie()
trie.add("hi")
trie.add("hello")
print(trie.search("hi"))
print(trie.search("hello"))
print(trie.search("hel"))
print(trie.search("hey"))
print(trie.head)
