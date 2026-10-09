# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        current=root
        res=[]
        while current is not None:
            if current.left is None:
                res.append(current.val)
                current=current.right
            else:
                predecessor=current.left

                while (predecessor.right is not None and predecessor.right!=current):
                    predecessor=predecessor.right
                if predecessor.right is None:
                    predecessor.right=current
                    current=current.left
                else:
                    predecessor.right=None
                    res.append(current.val)
                    current=current.right
        res.sort()
        return res[k-1]