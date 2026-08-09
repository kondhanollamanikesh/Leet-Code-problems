class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def solve(i, M):

            # No piles left
            if i == n:
                return 0

            # Can take everything
            if 2 * M >= n - i:
                return suffix[i]

            ans = 0

            for X in range(1, 2 * M + 1):

                newM = max(M, X)

                opponent = solve(i + X, newM)

                current = suffix[i] - opponent

                ans = max(ans, current)

            return ans

        return solve(0, 1)