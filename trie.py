class Trie:
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

    def insert(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.next[index]:
                node.next[index] = Trie()
            node = node.next[index]
        node.isEnd = True

    def search(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.next[index]:
                return False
            node = node.next[index]
        return node.isEnd

    def startsWith(self, prefix):
        node = self
        for c in prefix:
            index = ord(c) - ord("a")
            if not node.next[index]:
                return False
            node = node.next[index]
        return True
