class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans=[]
        def backtrack(index,size):
            nonlocal ans
            if len(size)==k :
                ans.append(size[:])
                return
            for i in range(index,n-(k - len(size)) + 2):
                size.append(i)
                backtrack(i+1,size)
                size.pop()
        backtrack(1,[])
        return ans