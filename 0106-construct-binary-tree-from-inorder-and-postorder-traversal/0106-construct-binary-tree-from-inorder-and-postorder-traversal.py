# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        pre_index = len(postorder)-1

        def backtrack(list1):
            nonlocal pre_index

            if not list1:
                return None

            root = TreeNode(postorder[pre_index])
            pre_index -= 1

            for i in range(len(list1)):
                if list1[i] == root.val:

                    root.right = backtrack(list1[i + 1:])
                    root.left = backtrack(list1[:i])
                    

                    return root

        return backtrack(inorder)