
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i == 0:
                    # Can only come from the left
                    grid[i][j] += grid[i][j - 1]

                elif j == 0:
                    # Can only come from above
                    grid[i][j] += grid[i - 1][j]

                else:
                    # Come from the cheaper of top and left
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]

