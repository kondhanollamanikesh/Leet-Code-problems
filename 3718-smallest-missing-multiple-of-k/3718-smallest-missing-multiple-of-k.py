class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        i = k

        while i in nums:
            i += k

        return i

