class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        grid_copy=deepcopy(grid)
        queue=deque()
        fresh_cnt=0
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==2:
                    queue.append((r,c))
                elif grid_copy[r][c]==1:
                    fresh_cnt+=1
        minutes=0
        while queue and fresh_cnt>0:
            minutes+=1
            rotten_len=len(queue)
            for _ in range(rotten_len):
                i,j=queue.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j=i+dx,j+dy
                    if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                        continue
                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2:
                        continue
                    fresh_cnt-=1
                    queue.append(((new_i),(new_j)))
                    grid_copy[new_i][new_j]=2
        if fresh_cnt>0:
            return -1
        return minutes