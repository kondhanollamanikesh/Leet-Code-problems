class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float("inf")

        while l <= r:
            initial = 0

            while initial + l <= len(nums):
                ans = sum(nums[initial:initial + l])

                if ans > 0:
                    mini = min(mini, ans)

                initial += 1

            l += 1

        if mini == float("inf"):
            return -1

        return mini