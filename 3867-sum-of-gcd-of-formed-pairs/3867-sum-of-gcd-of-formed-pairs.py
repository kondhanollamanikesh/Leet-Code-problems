class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Construct prefixGcd
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))

        # Step 2: Sort the prefixGcd array
        prefixGcd.sort()

        # Step 3: Form pairs and calculate the sum of GCDs
        left = 0
        right = n - 1
        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans