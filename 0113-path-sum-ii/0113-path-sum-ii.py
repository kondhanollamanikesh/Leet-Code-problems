# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans=[]
        sum1=[]
        def backtrack(node):
            if node is None:
                return 
            sum1.append(node.val)
            if node.left is None and node.right is None and sum(sum1)==targetSum:
                ans.append(sum1[:])
                sum1.pop()
                return
            backtrack(node.left)
            backtrack(node.right)
            sum1.pop()
        backtrack(root)
        return ans
