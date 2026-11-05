class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        prev=[-1]*cols
        for i in range(cols):
            prev[i]=matrix[rows-1][i]
        for i in range(rows-2,-1,-1):
            curr=[-1]*cols
            for j in range(cols):
                down=matrix[i][j]+prev[j]
                left_diag = float('inf')
                right_diag = float('inf')

                if j > 0:
                    left_diag = matrix[i][j] + prev[j-1]

                if j < cols-1:
                    right_diag = matrix[i][j] + prev[j+1]
                curr[j] = min(down, left_diag, right_diag)
            prev=curr.copy()
        return min(prev)
