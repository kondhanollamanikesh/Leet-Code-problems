class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[0],nums[len(nums)-1])
        
        