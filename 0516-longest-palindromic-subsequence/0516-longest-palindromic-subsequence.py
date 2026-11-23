class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s[::-1]
        n=len(s)
        prev= [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            curr = [0 for _ in range(n + 1)]
            for j in range(1, n + 1):

                if s[i - 1] == s1[j - 1]:
                    curr[j] = 1 + prev[j - 1]

                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev=curr
        return prev[n]