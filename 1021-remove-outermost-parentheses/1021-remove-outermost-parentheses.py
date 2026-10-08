class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    res += ch
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    res += ch

        return res
                