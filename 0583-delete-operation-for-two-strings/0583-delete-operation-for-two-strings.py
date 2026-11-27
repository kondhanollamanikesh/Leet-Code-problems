class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s = word1
        s1 = word2
        n = len(s)
        m = len(s1)

        prev = [0 for _ in range(m + 1)]

        for i in range(1, n + 1):
            curr = [0 for _ in range(m + 1)]

            for j in range(1, m + 1):

                if s[i - 1] == s1[j - 1]:
                    curr[j] = 1 + prev[j - 1]

                else:
                    curr[j] = max(prev[j], curr[j - 1])

            prev = curr

        return n + m - 2 * prev[m]