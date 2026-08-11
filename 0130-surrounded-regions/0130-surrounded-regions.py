class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        queue = deque()

        if rows <= 2 or cols <= 2:
            return

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Add only boundary O's
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                        queue.append([i, j])
                        visited[i][j] = 1

        # BFS
        while len(queue) != 0:
            i, j = queue.popleft()

            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < rows and
                    0 <= nj < cols and
                    board[ni][nj] == "O" and
                    visited[ni][nj] == 0):

                    visited[ni][nj] = 1
                    queue.append([ni, nj])

        # Convert surrounded O's to X
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 1:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"