class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        first=nums[0]
        last=nums[-1]
        s=set(nums)
        missing=[]
        for i in range(first,last+1):
            if i not in s:
                missing.append(i)
        return missing