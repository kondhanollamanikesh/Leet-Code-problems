class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd=[]
        even=[]
        for i in nums1:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        if not odd:
            return True

        # Find the smallest odd number
        smallest_odd = min(odd)

        res = []

        # Convert every even number to odd
        for i in even:
            if i > smallest_odd:
                res.append(i - smallest_odd)
            else:
                return False

        # Check all generated values
        for i in res:
            if i <= 0:
                return False

        return True