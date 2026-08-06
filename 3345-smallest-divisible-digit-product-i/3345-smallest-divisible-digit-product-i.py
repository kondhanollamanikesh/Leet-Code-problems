class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(num):
            p = 1
            while num > 0:
                p *= num % 10
                num //= 10
            return p

        while True:
            if product(n) % t == 0:
                return n
            n += 1