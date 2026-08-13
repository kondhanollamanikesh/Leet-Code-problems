class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        total=0
        final=float('-inf')
        while j<len(nums):
            total+=nums[j]
            if j-i+1>k:
                total-=nums[i]
                i+=1
            if j - i + 1 == k:
                final = max(final, total / k)
            j+=1
        return final