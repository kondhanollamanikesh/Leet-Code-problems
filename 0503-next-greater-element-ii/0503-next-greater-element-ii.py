class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        n1=len(nums)
        nums=nums + nums
        n=len(nums)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)!=0:
                if i<n1:
                    ans[i]=stack[-1]
                else:
                    stack.append(nums[i])
            stack.append(nums[i])
        return ans