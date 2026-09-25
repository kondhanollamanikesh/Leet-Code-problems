# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return False
        def check(left,right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False
            return check(left.left, right.right) and \
                   check(left.right, right.left)
        return check(root.left,root.right)