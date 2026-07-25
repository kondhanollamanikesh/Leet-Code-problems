class Solution:
    def maxProduct(self, n: int) -> int:
        largest=-1
        second=-1
        while n>0:
            d=n%10
            if d>largest:
                second=largest
                largest=d
            elif d>second:
                second=d
            n=n//10
        return largest*second
