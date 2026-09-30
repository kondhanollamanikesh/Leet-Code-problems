class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res=[0]*len(seq)
        depth=0
        for i in range(len(seq)):
            if seq[i]=='(':
                depth+=1
            
            res[i]=depth & 1
            if seq[i]==')':
                depth-=1
        return res