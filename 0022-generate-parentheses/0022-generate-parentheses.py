class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        lst1=[""]*(n*2)
        def solve(ind,left_count,right_count):
            if ind>=(n*2):
                result.append("".join(lst1))
                return
            if left_count<n:
                lst1[ind]="("
                solve(ind+1,left_count+1,right_count)
            if right_count<left_count:
                lst1[ind]=")"
                solve(ind+1,left_count,right_count+1)
        solve(0,0,0)
        return result    