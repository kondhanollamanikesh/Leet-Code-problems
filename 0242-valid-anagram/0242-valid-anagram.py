class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len (s)!=len(t):
            return False
        key = ''.join(sorted(s))
        key1=''.join(sorted(t))
        if key==key1:
            return True
        else:
            return False