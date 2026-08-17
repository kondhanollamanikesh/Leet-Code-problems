class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0

        def solve(grid, row1, col1, count):
            if row1 < 0 or row1 == len(grid) or col1 < 0 or col1 == len(grid[0]):
                return

            if visited[row1][col1] == 1:
                return

            if grid[row1][col1] == '0':
                return

            visited[row1][col1] = 1

            solve(grid, row1 + 1, col1, count)
            solve(grid, row1 - 1, col1, count)
            solve(grid, row1, col1 + 1, count)
            solve(grid, row1, col1 - 1, count)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    count += 1
                    solve(grid, i, j, count)

        return count