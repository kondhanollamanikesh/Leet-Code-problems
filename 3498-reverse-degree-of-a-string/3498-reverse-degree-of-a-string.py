class Solution:
    def reverseDegree(self, s: str) -> int:
        mul=0
        for i in range(len(s)):
            mul+=(26 - (ord(s[i]) - ord('a')))*(i+1)
        return mul