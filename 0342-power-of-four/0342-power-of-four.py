class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and 1073741824 % n == 0 and n % 3 == 1