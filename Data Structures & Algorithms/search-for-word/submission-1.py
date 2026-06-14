class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starting_points = []
        first_letter = word[0]
        dims_y, dims_x = len(board), len(board[0])
        for y in range(dims_y):
            row = board[y]
            for x in range(dims_x):
                if board[y][x] == first_letter:
                    starting_points.append((y,x))
        found = False
        def backtrack(last_pos, target_letter_id):
            if found: return

            next_pos = []
            if last_pos[0] < dims_y:
                next_pos.append((last_pos[0] + 1, last_pos[1])) 
            if last_pos[0] > 0:
                next_pos.append((last_pos[0] - 1, last_pos[1])) 
            if last_pos[1] < dims_x:
                next_pos.append((last_pos[0], last_pos[1] + 1)) 
            if last_pos[1] > 0:
                next_pos.append((last_pos[0], last_pos[1] - 1))
            
            for p in next_pos:
                cur_y, cur_x = p[0], p[1]
                current_letter = board[y][x]
                if current_letter == word[target_letter_id]:
                    if target_letter_id == len(word) - 1:
                        found = True
                        return
                    
                    backtrack(p, target_letter_id + 1)

        return found