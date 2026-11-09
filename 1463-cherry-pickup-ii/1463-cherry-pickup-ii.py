class Solution:
    def solve(self,i,j1,j2,grid,dp):
        if j1<0 or j1>=cols or j2<0 or j2>=cols:
            return float("-inf")
        if i==rows-1:
            if j1==j2:
                return grid[i][j1]
            return grid[i][j1] + grid[i][j2]
        maxi=0
        for new_j1 in range(-1,2):
            for new_j2 in range(-1,2):
                if j1==j2:
                    ans=grid[i][j1] + dp[i][new_j1][new_j2]
                else:
                    ans=grid[i][j1] + dp[i][new_j1][new_j2] + grid[i][j2]
                maxi=max(maxi,ans)
        dp[i][j1][j2]=maxi
        return dp[i][j1][j2]

    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dp=[[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
        for j1 in range(cols):
            for j2 in range(cols):
                if j1 == j2:
                    dp[rows-1][j1][j2] = grid[rows-1][j1]
                else:
                    dp[rows-1][j1][j2] = (
                        grid[rows-1][j1] + grid[rows-1][j2]
                    )
        for i in range(rows-2, -1, -1):
            for j1 in range(cols):
                for j2 in range(cols):

                    maxi = float("-inf")

                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):

                            new_j1 = j1 + dj1
                            new_j2 = j2 + dj2

                            if (0 <= new_j1 < cols and
                                0 <= new_j2 < cols):

                                if j1 == j2:
                                    ans = grid[i][j1] + dp[i+1][new_j1][new_j2]
                                else:
                                    ans = (grid[i][j1] + grid[i][j2]
                                           + dp[i+1][new_j1][new_j2])

                                maxi = max(maxi, ans)

                    dp[i][j1][j2] = maxi

        return dp[0][0][cols-1]