class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            if index == len(word):
                return node.end

            letter = word[index]
            
            if letter == ".":
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            if letter not in node.children:
                return False
            
            return dfs(index+1, node.children[letter])
        return dfs(0, self.root)