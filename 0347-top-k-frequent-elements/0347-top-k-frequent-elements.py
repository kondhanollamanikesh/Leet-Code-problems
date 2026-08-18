class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count=Counter(nums)
        l=0
        lst1=[]
        for key,value in count.most_common():
            if l<k :
                l+=1
                lst1.append(key)
            else:
                break
        return lst1