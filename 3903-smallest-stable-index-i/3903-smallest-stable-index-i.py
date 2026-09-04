class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=[]
        i=0
        j=0
        while j<len(nums):
            maxi=max(nums[i:j+1])
            mini=min(nums[j:])
            if maxi-mini<=k:
                return j
            j+=1
        return -1