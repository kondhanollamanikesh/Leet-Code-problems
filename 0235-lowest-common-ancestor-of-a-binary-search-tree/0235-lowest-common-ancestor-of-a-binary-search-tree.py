# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []

        temp = root
        while temp:
            path1.append(temp)

            if p.val < temp.val:
                temp = temp.left
            elif p.val > temp.val:
                temp = temp.right
            else:
                break

        temp = root
        while temp:
            path2.append(temp)

            if q.val < temp.val:
                temp = temp.left
            elif q.val > temp.val:
                temp = temp.right
            else:
                break

        lca = None

        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                lca = path1[i]
            else:
                break

        return lca
