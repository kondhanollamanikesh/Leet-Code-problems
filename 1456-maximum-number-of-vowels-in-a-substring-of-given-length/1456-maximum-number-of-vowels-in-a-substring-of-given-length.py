class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        right=0
        count=0
        final_count=0
        while right<len(s):
            if s[right] in 'aeiou':
                count+=1
            while (right-left)+1>k:
                if s[left] in 'aeiou':
                    count -= 1
                left+=1 
            final_count=max(count,final_count)
                
            right+=1
        return final_count
                