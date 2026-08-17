class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum=0
        hashmap = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in hashmap:
                if i - hashmap[remainder] >= 2:
                    return True
            else:
                hashmap[remainder] = i

        return False