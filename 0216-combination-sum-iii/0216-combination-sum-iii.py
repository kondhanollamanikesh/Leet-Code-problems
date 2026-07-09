class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        result=[]
        def solve(ind,total,subset):
            if total==n and len(subset)==k:
                result.append(subset.copy())
                return
            if ind == len(nums):
                return
            subset.append(nums[ind])
            solve(ind+1,total+nums[ind],subset)
            subset.pop()
            solve(ind+1,total,subset)
        solve(0,0,[])
        return result