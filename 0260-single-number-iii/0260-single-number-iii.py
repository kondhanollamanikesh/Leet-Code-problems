class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        group1 = []
        group2 = []
        res = []
        ans1 = 0
        ans2 = 0
        xor = 0

        # XOR all numbers
        for i in nums:
            xor ^= i

        # Find rightmost set bit
        diff_bit = xor & -xor

        for i in nums:
            if i & diff_bit == 0:
                group1.append(i)
            else:
                group2.append(i)

        for i in group1:
            ans1 ^= i

        for i in group2:
            ans2 ^= i

        res.append(ans1)
        res.append(ans2)

        return res