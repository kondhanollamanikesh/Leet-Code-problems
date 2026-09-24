class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):

            num = nums[i]
            ans = 0

            while num > 0:
                digit = num % 10
                ans = ans + digit
                num = num // 10

            if ans == i:
                return i

        return -1