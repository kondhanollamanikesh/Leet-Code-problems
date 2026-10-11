class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(0,n):
            if n%(i+1)==0:
                res+=nums[i]*nums[i]
            else:
                continue
        return res