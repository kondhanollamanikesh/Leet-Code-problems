class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        ans=0
        left=0
        right=0
        while right < len(nums):
            if nums[right] not in freq:
                    freq[nums[right]] = 1
            else:
                freq[nums[right]] += 1
            while freq[nums[right]] > k:
                    freq[nums[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans