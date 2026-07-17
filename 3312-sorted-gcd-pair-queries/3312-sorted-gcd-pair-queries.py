class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cnt[g] += freq[multiple]
        gcdPairs = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            gcdPairs[g] = cnt[g] * (cnt[g] - 1) // 2
            for multiple in range(2 * g, mx + 1, g):
                gcdPairs[g] -= gcdPairs[multiple]
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + gcdPairs[g]
        ans = []
        for q in queries:
            # q is 0-indexed
            ans.append(bisect_left(prefix, q + 1))
        return ans