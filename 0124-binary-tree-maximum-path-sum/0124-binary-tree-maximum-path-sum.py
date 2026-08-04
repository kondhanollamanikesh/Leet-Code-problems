# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final=float('-inf')
        def solve(node):
            nonlocal final

            if node is None:
                return 0

            left = max(solve(node.left), 0)
            right = max(solve(node.right), 0)

            # Update the maximum path sum passing through this node
            final = max(final, left + right + node.val)

            # Return the maximum gain to the parent
            return node.val + max(left, right)

        solve(root)
        return final