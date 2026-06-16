class Solution:
    def is_valid(self, board):
        n = len(board)
        for i in range(n):
            for j in range(i+1, n):
                if board[i] == -1 or board[j] == -1:
                    continue
                # same col, duplicate number in 2 rows
                if board[i] == board[j]:
                    return False
                
                if abs(board[i] - board[j]) == abs(i-j):
                    return False
        return True
    
    def board_to_results(self, board):
        n = len(board)
        placeholder = [['.'] * n for _ in range(n)]
        for row in range(n):
            queen_pos = board[row]
            placeholder[row][queen_pos] = 'Q'
        return [''.join(row) for row in placeholder]

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [-1] * n
        # board[n] is position of queen in a n-th row
        results = []
        def dfs(nth_queen):
            if not self.is_valid(board):
                return False
            if nth_queen == n:
                results.append(self.board_to_results(board))
                return True
            for col in range(n):
                board[nth_queen] = col
                dfs(nth_queen + 1)
                board[nth_queen] = -1
        dfs(0)
        return [self.board_to_results(b) for b in results]