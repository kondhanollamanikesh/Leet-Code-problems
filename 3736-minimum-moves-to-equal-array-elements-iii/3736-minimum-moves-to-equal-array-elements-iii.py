class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi=max(nums)
        res=0
        for i in nums:
            res+=maxi-i
        return res