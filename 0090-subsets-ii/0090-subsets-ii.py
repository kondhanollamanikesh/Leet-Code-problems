class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        total_subsets=1<<n
        result=set()
        for num in range(total_subsets):
            lst=[]
            for i in range(n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            result.add(tuple(lst))
        return [list(x) for x in result]