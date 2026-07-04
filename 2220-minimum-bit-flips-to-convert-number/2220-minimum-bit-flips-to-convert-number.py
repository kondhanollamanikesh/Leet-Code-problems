class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result=start^goal
        count=0
        for i in range(32):
            if result&(1<<i)!=0:
                count+=1
        return count 