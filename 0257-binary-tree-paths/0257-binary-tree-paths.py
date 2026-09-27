# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        ans=[]
        paths=[]
        def backtrack(node):
            if node is None:
                return
            paths.append(node.val)
            if node.left is None and node.right is None:
                ans.append(paths.copy())
                paths.pop()
                return
            
            
            backtrack(node.left)
            
            backtrack(node.right)
            paths.pop()
        backtrack(root)
        result=["->".join(map(str, path)) for path in ans]    
        return result
            