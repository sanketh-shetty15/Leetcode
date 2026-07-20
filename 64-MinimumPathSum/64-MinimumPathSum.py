# Last updated: 20/07/2026, 18:40:03
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j != 0:
                        grid[i][j] = grid[i][j-1] + grid[i][j]
                    else:
                        grid[i][j] = grid[i][j]
                else:
                    if j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i - 1][j] + grid[i][j] , grid[i][j-1] + grid[i][j])
        return grid[m-1][n-1]