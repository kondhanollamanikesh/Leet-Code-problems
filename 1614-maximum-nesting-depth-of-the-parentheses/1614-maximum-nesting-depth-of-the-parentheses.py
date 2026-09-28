class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_count=0
        for i in s:
            if i=="(":
                count+=1
            elif i==")":
                max_count=max(max_count,count)
                count-=1
        return max_count