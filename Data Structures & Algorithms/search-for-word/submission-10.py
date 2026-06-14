class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dims_y, dims_x = len(board), len(board[0])
        def backtrack(y, x, i) -> bool:
            # core idea:
            # check from upper left to bottom right
            # if matching, return true

            if board[y][x] != word[i]:
                return False
            if len(word) == i + 1:
                return True
            val = board[y][x]
            board[y][x] = "#"
            next_pos = [] 
            if y+1 < dims_y: 
                next_pos.append(y + 1, x)
            if y > 0: 
                next_pos.append(y - 1, x)
            if x+1 < dims_x: 
                next_pos.append(y, x + 1)
            if x > 0: 
                next_pos.append(y, x - 1)
            for pos in next_pos:
                if backtrack(pos[0], pos[1], i+1):
                    return True
            board[y][x] = val
        for y in range(dims_y):
            for x in range(dims_x):
                if board[y][x] == word[0]:
                    if backtrack(y,x,0):
                        return True
        return False