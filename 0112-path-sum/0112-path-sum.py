# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def backtrack(root1,sum1):
            if root1 is None:
                return False


            sum1 += root1.val

            if root1.left is None and root1.right is None:
                return sum1 == targetSum

            return backtrack(root1.left, sum1) or backtrack(root1.right, sum1)
        return backtrack(root,0)