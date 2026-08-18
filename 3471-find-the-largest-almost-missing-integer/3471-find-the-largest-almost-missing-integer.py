class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        i = nums[0]
        j = nums[-1]

        if len(nums) == k:
            return max(nums)

        if k == 1:
            ans = -1

            for x in nums:
                if nums.count(x) == 1:
                    if x > ans:
                        ans = x

            return ans

        if i not in nums[1:] and j not in nums[:-1]:
            if i > j:
                return i
            else:
                return j

        if i not in nums[1:] and j in nums[:-1]:
            return i

        if i in nums[1:] and j not in nums[:-1]:
            return j

        else:
            return -1