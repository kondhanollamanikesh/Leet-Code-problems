class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        rows=len(triangle)
        dp=[[-1 for _ in range(i+1)] for i in range(rows)]
        for i in range(rows-1,-1,-1):
            for j in range(i,-1,-1):
                if i==rows-1:
                    dp[i][j]=triangle[i][j]
                    continue
                up=float("inf")
                diag=float("inf")
                if i+1<rows and j+1<len(dp[i+1]):
                    diag = dp[i + 1][j + 1]
                if i+1<rows:
                    up = dp[i + 1][j]
                dp[i][j] = triangle[i][j] + min(up, diag)
        return dp[0][0]