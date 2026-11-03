class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i==rows-1 and j==cols-1:
                    dp[i][j]=grid[i][j]
                    continue
                right = float('inf')
                down = float('inf')

                if j+1 < cols:
                    right = dp[i][j+1]

                if i+1 < rows:
                    down = dp[i+1][j]

                dp[i][j] = grid[i][j] + min(right, down)

        return dp[0][0]