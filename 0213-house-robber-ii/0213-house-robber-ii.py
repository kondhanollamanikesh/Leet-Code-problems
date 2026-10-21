class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1=0
        prev2=0
        for money in nums[1:]:
            curr=max(prev1,prev2+money)
            prev2=prev1
            prev1=curr 
        ans1=prev1

        prev1=0
        prev2=0   
        
        for i in range(len(nums)-1):
            curr=max(prev1,prev2+nums[i])
            prev2=prev1
            prev1=curr
        ans2=prev1


        return max(ans1,ans2)