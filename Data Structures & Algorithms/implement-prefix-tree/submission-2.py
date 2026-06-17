class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, letter in enumerate(word):
            if letter not in curr.children:
                new_node = TrieNode() 
                curr.children[letter] = new_node

            curr = curr.children[letter]
            if i == len(word) - 1:
                curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i, letter in enumerate(word):
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.end
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i, letter in enumerate(prefix):
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True