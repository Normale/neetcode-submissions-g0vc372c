from itertools import product
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word
    
class Solution:
    def _get_valid_positions(self, dims_x, dims_y, x, y):
        result = []

        if y+1 < dims_y:
            result.append((y+1, x))
        if y - 1 >= 0:
            result.append((y-1, x))
        if x + 1 < dims_x:
            result.append((y, x+1))
        if x - 1 >= 0:
            result.append((y, x-1))
        return result

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dims_y, dims_x = len(board), len(board[0])

        t = Trie()
        for word in words:
            t.insert_word(word)

        result = set()
        def dfs(x, y, child):
            letter, node = child

            val = board[y][x] # B
            if val != letter:
                return
            if node.word:
                result.add(node.word)

            board[y][x] = "#"

            valid_positions = self._get_valid_positions(dims_x, dims_y, x, y)
            for pos in valid_positions:
                new_y, new_x = pos[0], pos[1]
                for c in node.children.items():
                    dfs(new_x, new_y, c)
            board[y][x] = val
            return 

        for y, x in product(range(dims_y), range(dims_x)):
            for c in t.root.children.items():
                dfs(x,y,c)

        return list(result)