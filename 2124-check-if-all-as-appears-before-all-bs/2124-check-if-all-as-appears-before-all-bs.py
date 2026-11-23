class Solution:
    def checkString(self, s: str) -> bool:
        curr=""
        prev=""
        a=0
        b=1
        while b<len(s):
            prev=s[a]
            curr=s[b]
            if prev=="b" and curr=='a':
                return False
            a+=1
            b+=1
        return True