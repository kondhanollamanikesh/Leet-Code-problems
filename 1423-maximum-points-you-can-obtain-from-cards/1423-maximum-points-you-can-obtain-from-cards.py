class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        ans=0
        if k==n:
            ans = reduce(lambda x, y: x + y, cardPoints)
            return ans
        maxi=0
        left_sum=0
        right_sum=0
        for i in range(k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_index=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_index]
            maxi=max(maxi,left_sum+right_sum)
            right_index-=1
        return maxi