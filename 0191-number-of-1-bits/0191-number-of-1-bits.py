class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = []

        while n > 0:
            binary.append(n % 2)
            n = n // 2

        binary.reverse()
        count=0
        for i in binary:
            if i==1:
                count+=1
        return count