class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        ans = 0

        for i, value in enumerate(freq):
            pushes = i // 8 + 1
            ans += pushes * value

        return ans