# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        pre_index = 0

        def backtrack(list1):
            nonlocal pre_index

            if not list1:
                return None

            root = TreeNode(preorder[pre_index])
            pre_index += 1

            for i in range(len(list1)):
                if list1[i] == root.val:

                    root.left = backtrack(list1[:i])
                    root.right = backtrack(list1[i + 1:])

                    return root

        return backtrack(inorder)