class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(k, nums[-1] + k + 1, k):
            if i not in nums:
                return i

