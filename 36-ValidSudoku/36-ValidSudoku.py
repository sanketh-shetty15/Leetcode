# Last updated: 20/07/2026, 18:40:18
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = set()
            for c in row:
                if c != '.':
                    if c in seen:
                        return False
                    seen.add(c)

        for col in range(9):
            seen = set()
            for row in range(9):
                c = board[row][col]
                if c != '.':
                    if c in seen:
                        return False
                    seen.add(c)

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        val = board[r][c]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True
