# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue=deque([(root,None)])
        while queue:
            x_parent = None
            y_parent = None

            for _ in range(len(queue)):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent

                if node.val == y:
                    y_parent = parent

                if node.left is not None:
                    queue.append((node.left, node))

                if node.right is not None:
                    queue.append((node.right, node))
            if x_parent is not None and y_parent is not None:
                return x_parent!=y_parent
            if x_parent is not None and y_parent is None:
                return False
        return False