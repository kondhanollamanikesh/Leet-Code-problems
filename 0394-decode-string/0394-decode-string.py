class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)

            else:
                curr = ""

                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr

                stack.pop()  # Remove '['

                num = ""

                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(curr * int(num))

        return "".join(stack)