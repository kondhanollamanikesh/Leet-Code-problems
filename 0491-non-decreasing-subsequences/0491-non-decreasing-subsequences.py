class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res=[]
        ans=[]
        def backtrack(index):
            if len(ans) >= 2:
                res.append(ans[:])
            used = set()

            for i in range(index, len(nums)):
                if nums[i] in used:
                    continue

                if not ans or nums[i] >= ans[-1]:
                    used.add(nums[i])
                    ans.append(nums[i])

                    backtrack(i + 1)

                    ans.pop()
        backtrack(0)
        return res