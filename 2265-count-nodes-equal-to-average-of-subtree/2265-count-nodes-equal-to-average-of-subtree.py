# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def preorder(root):
            nonlocal ans

            if root is None:
                return 0, 0

            left_sum, left_count = preorder(root.left)
            right_sum, right_count = preorder(root.right)

            sum1 = left_sum + right_sum + root.val
            count = left_count + right_count + 1

            avg = sum1 // count

            if root.val == avg:
                ans += 1

            return sum1, count

        preorder(root)

        return ans