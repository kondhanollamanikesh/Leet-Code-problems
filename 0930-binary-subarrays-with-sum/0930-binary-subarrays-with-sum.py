class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum1=0
        count=0
        mp={0:1}
        for i in nums:
            sum1+=i
            if sum1-goal in mp:
                count+=mp[sum1-goal]
            if sum1 in mp:
                mp[sum1]+=1
            else:
                mp[sum1]=1
        return count