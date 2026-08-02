class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(left, right):

            if left == right:
                return piles[left]

            if (left, right) in memo:
                return memo[(left, right)]

            takeLeft = piles[left] - dfs(left + 1, right)

            takeRight = piles[right] - dfs(left, right - 1)

            memo[(left, right)] = max(takeLeft, takeRight)

            return memo[(left, right)]

        return dfs(0, len(piles)-1) > 0