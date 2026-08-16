class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i=0
        j=0
        sum1=0
        count=0
        count1=0
        while j<len(arr):
            sum1+=arr[j]
            count+=1
            while count>k :
                sum1-=arr[i]
                count-=1
                i+=1
            if sum1>=k*threshold and count==k:
                count1+=1
            j+=1
        return count1
