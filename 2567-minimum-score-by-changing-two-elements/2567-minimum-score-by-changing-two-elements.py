class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        # Only four smallest/largest boundary elements matter.
        scores = []

        scores.append(nums[n-1] - nums[2])
        scores.append(nums[n-2] - nums[1])
        scores.append(nums[n-3] - nums[0])
        scores.append(nums[n-1] - nums[0])

        return min(scores)