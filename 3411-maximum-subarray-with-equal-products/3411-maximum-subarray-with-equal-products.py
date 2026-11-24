class Solution:
    def maxLength(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] * nums[i])
        maxi = 1
        n = len(nums)

        for i in range(n):
            for j in range(i, n):

                # Calculate product
                if i == 0:
                    product = prefix[j]
                else:
                    product = prefix[j] // prefix[i - 1]

                # Calculate GCD and LCM
                gcd = 0
                lcm = 1

                for k in range(i, j + 1):
                    gcd = math.gcd(gcd, nums[k])
                    lcm = math.lcm(lcm, nums[k])

                # Check product equivalence
                if product == gcd * lcm:
                    maxi = max(maxi, j - i + 1)

        return maxi
