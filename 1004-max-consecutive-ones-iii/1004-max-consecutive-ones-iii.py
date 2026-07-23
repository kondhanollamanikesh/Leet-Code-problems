class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        left=0
        right=0
        n=len(nums)
        zeros=0
        while right<n:
            
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi