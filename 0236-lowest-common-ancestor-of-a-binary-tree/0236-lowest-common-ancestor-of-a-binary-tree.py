# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_route = []
        q_route = []

        def backtrack(node, route, target):

            if node is None:
                return False

            route.append(node)

            if node == target:
                return True

            if backtrack(node.left, route, target):
                return True

            if backtrack(node.right, route, target):
                return True

            route.pop()
            return False

        backtrack(root, p_route, p)
        backtrack(root, q_route, q)

        i = 0

        while i < len(p_route) and i < len(q_route):
            if p_route[i] != q_route[i]:
                break
            i += 1

        return p_route[i - 1]