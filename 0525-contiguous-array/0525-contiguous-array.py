class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum=0
        max_len=0

        hash_map={0:-1}

        for i in range(len(nums)):
            if nums[i]==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            
            if prefix_sum in hash_map:
                length=i-hash_map[prefix_sum]
                max_len=max(max_len,length)
            else:
                hash_map[prefix_sum]=i

        return max_len