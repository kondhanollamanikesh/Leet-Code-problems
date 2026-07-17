class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        stack = []
        rev = ""

        for ch in str(x):
            stack.append(ch)

        while stack:
            rev += stack.pop()

        return str(x) == rev