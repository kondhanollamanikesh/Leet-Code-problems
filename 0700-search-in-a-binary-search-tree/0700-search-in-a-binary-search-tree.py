# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def backtrack(node):
            if node is None:
                return None

            if node.val == val:
                return node

            elif node.val > val:
                return backtrack(node.left)

            else:
                return backtrack(node.right)

        return backtrack(root)