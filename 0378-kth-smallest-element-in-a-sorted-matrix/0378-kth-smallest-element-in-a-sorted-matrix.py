class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            count = 0
            col = n - 1

            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += col + 1

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left