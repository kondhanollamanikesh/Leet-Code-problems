class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}
        maxi = 0

        for num in nums:
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1

            maxi = max(maxi, dp[num], dp[num + 1])

        return maxi
            