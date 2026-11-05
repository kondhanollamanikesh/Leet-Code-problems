class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in range(len(arr1)):
            valid=True
            for j in range(len(arr2)):
                dist=abs(arr1[i]-arr2[j])
                if dist<=d:
                    valid=False
                    continue 
            if valid:   
                count+=1
        return count