class Solution:
    def minChanges(self, s: str) -> int:
        i=0
        counter=0
        while i < len(s):
            if s[i] != s[i+1]:
                counter += 1

            i += 2

        return counter

            