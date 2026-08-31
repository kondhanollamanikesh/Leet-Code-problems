class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        i = 0
        sign = 1
        num = 0

        # Handle sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        elif i < len(s) and s[i] == '+':
            i += 1

        # Read digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # 32-bit integer range
        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num