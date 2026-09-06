class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        priority_queue=[]
        heapq.heappush(priority_queue,[0,0,0])
        dist=[[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        while len(priority_queue)!=0:
            curr_effort,curr_row,curr_col=heapq.heappop(priority_queue)
            if curr_row == rows - 1 and curr_col == cols - 1:
                return curr_effort
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_row,new_col=i+curr_row,j+curr_col
                if new_row<0 or new_row==rows or new_col<0 or new_col==cols:
                    continue
                diff = abs(
                    heights[curr_row][curr_col] -
                    heights[new_row][new_col]
                )
                new_effort = max(curr_effort, diff)
                if new_effort<dist[new_row][new_col]:
                    dist[new_row][new_col]=new_effort
                    heapq.heappush(priority_queue,[new_effort,new_row,new_col])
        return -1