class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        leftrow=[0]*n
        ud=[0]*((2*n)-1)
        ld=[0]*((2*n)-1)
        board=["."*n for _ in range(n)]
        def solve(col,board,result,leftrow,ud,ld,n):
            if col==n:
                result.append(board[:])
                return
            for row in range(n):
                if(leftrow[row]==0 and ld[row+col]==0 and ud[n-1+col-row]==0):
                    board[row]=board[row][:col]+"Q"+board[row][col+1:]
                    leftrow[row]=1
                    ld[row+col]=1
                    ud[n-1+col-row]=1
                    solve(col+1,board,result,leftrow,ud,ld,n)
                    board[row]=board[row][:col]+"."+board[row][col+1:]
                    leftrow[row]=0
                    ld[row+col]=0
                    ud[n-1+col-row]=0
        solve(0,board,result,leftrow,ud,ld,n)
        return result