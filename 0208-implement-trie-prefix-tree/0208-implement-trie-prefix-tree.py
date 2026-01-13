class Node:
    def __init__(self):
        self.bitmap = 0
        self.child = []
        self.complete = False
    
    def i(self, char: str) -> int:
        return ord(char) - ord('a')

    def i_bit(self, char: str) -> int:
        return 1 << self.i(char)

    def i_index(self, char: str) -> int:
        return bin(self.bitmap & (self.i_bit(char) - 1)).count('1')

    def has_child(self, char: str) -> bool:
        return (self.bitmap & self.i_bit(char)) != 0

    def get_child(self, char: str) -> "Node":
        if not self.has_child(char):
            return None

        return self.child[self.i_index(char)]

    def add_child(self, char: str, node: "Node") -> None:
        # It's about update, which doesn't be needed 
        # if has_child(char):
        #     self.children[self.i_index(char)] = node
        #     return

        self.child.insert(self.i_index(char), node)
        self.bitmap |= self.i_bit(char)

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.has_child(c):
                node.add_child(c, Node())
            node = node.get_child(c)
        node.complete = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.has_child(c):
                node = node.get_child(c)
            else:
                return False
        return node.complete

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.has_child(c):
                node = node.get_child(c)
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)