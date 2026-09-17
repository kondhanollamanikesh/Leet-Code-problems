class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(combo):
            nonlocal ans
            if len(nums)==len(combo):
                ans.append(combo[:])
                return
            for i in range(len(nums)):
                if nums[i] not in combo:
                    combo.append(nums[i])
                    backtrack(combo)
                    combo.pop()

        backtrack([])
        return ans