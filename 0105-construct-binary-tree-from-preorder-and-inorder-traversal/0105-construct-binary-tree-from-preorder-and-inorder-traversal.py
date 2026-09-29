# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        root = TreeNode(preorder[0])
        pre_index = 0

        def backtrack(root, list1):
            nonlocal pre_index

            if root is None or not list1:
                return None

            for i in range(len(list1)):

                if list1[i] == root.val:

                    pre_index += 1

                    if pre_index < len(preorder):
                        root.left = backtrack(
                            TreeNode(preorder[pre_index]),
                            list1[:i]
                        )

                    if pre_index < len(preorder):
                        root.right = backtrack(
                            TreeNode(preorder[pre_index]),
                            list1[i + 1:]
                        )

                    return root

            return root

        return backtrack(root, inorder)