class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i==m-1 and j==n-1:
                    dp[i][j]=1
                    continue
                count=0
                for x,y in [(0,1),(1,0)]:
                    new_i,new_j=i+x,j+y
                    if new_i>=m or new_j>=n:
                        continue
                    count+= dp[new_i][new_j]
                dp[i][j]=count
        return dp[0][0]