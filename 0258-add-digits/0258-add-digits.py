class Solution:
    def addDigits(self, num: int) -> int:
        def add(n):
            s=str(n)
            su=0
            if len(s)>1:
                for i in s:
                    su+=int(i)
            else:
                return n
            return su
        ans=add(num)
        s1=str(ans)

        while len(str(ans)) > 1:
            ans = add(ans)
        return ans