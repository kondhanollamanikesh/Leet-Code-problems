class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        maxi = 0

        for ch in s:
            while ch in stack:
                stack.pop(0)  

            stack.append(ch)
            maxi = max(maxi, len(stack))

        return maxi