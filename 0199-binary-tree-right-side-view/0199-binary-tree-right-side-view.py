# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def reversepostorder(node,level,ans):
            if node==None:
                return
            if level==len(ans):
                ans.append(node.val)
            if node.right:
                reversepostorder(node.right,level+1,ans)
            if node.left:
                reversepostorder(node.left,level+1,ans)
        reversepostorder(root,0,ans)
        return ans