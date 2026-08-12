class Solution:
    def reverse(self, x: int) -> int:
        rever=0
        sign = -1 if x < 0 else 1
        x=abs(x)
        while x>0:
            digit=x%10
            rever=rever*10+digit
            x//=10
        rever=sign * rever
        if -2147483648<=rever<=2147483647:
            return rever
        else:
            return 0

