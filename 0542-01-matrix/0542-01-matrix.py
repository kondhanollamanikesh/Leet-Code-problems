class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            u, v = queue.popleft()

            for x, y in directions:
                new_i = u + x
                new_j = v + y

                # Out of bounds
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                # Already visited
                if mat[new_i][new_j] != -1:
                    continue

                # Set distance
                mat[new_i][new_j] = mat[u][v] + 1

                queue.append((new_i, new_j))

        return mat