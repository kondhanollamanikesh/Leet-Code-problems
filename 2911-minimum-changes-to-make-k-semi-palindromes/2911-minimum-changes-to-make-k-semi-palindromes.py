class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):

                length = j - i + 1
                mini = float('inf')

                # Find valid divisors
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Compare characters in each group
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    mini = min(mini, changes)

                cost[i][j] = mini

        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0]=0
        for parts in range(1,k+1):
            for i in range(2 * parts,n+1):
                for j in range(2 * (parts - 1),i):
                    if i - j <2:
                        continue
                    if dp[parts - 1][j] == float('inf'):
                        continue
                    dp[parts][i] = min(
                            dp[parts][i],
                            dp[parts - 1][j] + cost[j][i - 1]
                        )
        return dp[k][n]            


