class Solution:
    def checkDivisibility(self, n: int) -> bool:
        su=0
        pro=1
        ans=0
        s=str(n)
        for i in s:
            su+=int(i)
            pro*=int(i)
        ans=su+pro
        if n%ans==0:
            return True
        else:
            return False
