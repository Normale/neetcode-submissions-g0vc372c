class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = [set() for i in range(9)]
        horizontal = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for y in range(9):
            for x in range(9):
                val = board[y][x]
                if val == ".":
                    continue
                col = horizontal[y]
                row = vertical[x]
                square = squares[3 * (y//3) + (x//3)]
                if val in horizontal[y]:
                    print(f"{x=}{y=}")
                    print(f"H returning false in {horizontal[y]}, duplicate {val}")
                    return False
                if val in vertical[x]:
                    print(f"{x=}{y=}")
                    print(f"V returning false in {vertical[y]}, duplicate {val}")
                    return False
                if val in square:
                    print(f"{x=}{y=}")
                    print(f"S returning false in {squares[ 3 * y//3 + x//3]}, duplicate {val}")
                    return False
                horizontal[y].add(val)
                vertical[x].add(val)
                squares[ 3 * (y//3) + x//3].add(val)
        return True