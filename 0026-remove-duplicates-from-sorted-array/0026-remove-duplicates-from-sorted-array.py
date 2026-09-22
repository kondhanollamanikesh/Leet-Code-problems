class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        count = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = "_"
            else:
                i = j
                count += 1

            j += 1

        nums.sort(key=lambda x: x == "_")

        return count