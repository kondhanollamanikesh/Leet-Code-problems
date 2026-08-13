class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        tar = 0
        length = float('inf')

        while j < len(nums):
            tar += nums[j]

            while tar >= target:
                length = min(length, j - i + 1)
                tar -= nums[i]
                i += 1

            j += 1

        if length == float('inf'):
            return 0

        return length