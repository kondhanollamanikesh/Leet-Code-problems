class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        if len(nums) == 0:
            return []

        for i in range(len(nums)):

            if i == 0:
                arr1.append(nums[i])

            elif i == 1:
                arr2.append(nums[i])

            else:
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

        return arr1 + arr2