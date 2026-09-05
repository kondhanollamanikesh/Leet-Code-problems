class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        if grid[0][0] == 1:
            return -1
        elif grid[rows-1][cols-1]==1:
            return -1
        if rows == 1 and cols == 1:
            return 1
        dist=[[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        priority_queue=[]
        heapq.heappush(priority_queue, (1, 0, 0))
        while len(priority_queue)!=0:
            dis,row,col = heapq.heappop(priority_queue)
            for i,j in [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]:
                new_row,new_col=i+row,j+col
                if new_row<0 or new_row==rows or new_col<0 or new_col==cols:
                    continue
                if grid[new_row][new_col]==1:
                    continue
                dis_trav=dis+1
                if dis_trav<dist[new_row][new_col]:
                    dist[new_row][new_col]=dis_trav
                    heapq.heappush(priority_queue,[dis_trav,new_row,new_col])
        if dist[rows - 1][cols - 1] == sys.maxsize:
            return -1
        return dist[rows-1][cols-1]