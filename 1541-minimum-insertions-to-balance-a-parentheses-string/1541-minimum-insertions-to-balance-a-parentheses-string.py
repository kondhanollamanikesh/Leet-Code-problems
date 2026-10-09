class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
                i += 1

            else:
                if i + 1 < len(s) and s[i + 1] == ")":
                    if stack:
                        stack.pop()
                    else:
                        count += 1
                    i += 2

                else:
                    if stack:
                        stack.pop()
                        count += 1
                    else:
                        count += 2
                    i += 1

        return count + 2 * len(stack)