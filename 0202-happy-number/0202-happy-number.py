class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total

        num = n
        seen = set()

        while True:

            if num == 1:
                return True

            if num in seen:
                return False

            seen.add(num)

            num = get_next(num)