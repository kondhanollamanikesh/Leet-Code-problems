class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hash_map={}
        for i in range(len(nums2)):
            
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                hash_map[num]=nums2[i]
            stack.append(nums2[i])
        while stack:
            num = stack.pop()
            hash_map[num] = -1
        ans=[]
        for num in nums1:
            ans.append(hash_map[num])
        return ans
