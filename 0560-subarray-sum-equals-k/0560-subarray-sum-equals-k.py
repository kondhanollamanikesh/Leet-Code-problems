class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            sum1 += num

            if sum1 - k in mp:
                count += mp[sum1 - k]

            if sum1 in mp:
                mp[sum1] += 1
            else:
                mp[sum1] = 1

        return count