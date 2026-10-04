# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)
        temp=root
        while temp is not None:
            if temp.val<val:
                if temp.right is None:
                    temp.right=TreeNode(val)
                    break
                temp=temp.right
            else:
                if temp.left is None:
                    temp.left=TreeNode(val)
                    break
                temp=temp.left
        return root