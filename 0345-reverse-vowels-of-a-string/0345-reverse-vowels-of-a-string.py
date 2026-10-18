class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        vow='aeiouAEIOU'
        while j>i:
            if s[i] not in vow:
                i += 1
            elif s[j] not in vow:
                j -= 1
            else:
                s[j],s[i]=s[i],s[j]
                i+=1
                j-=1
        return "".join(s)