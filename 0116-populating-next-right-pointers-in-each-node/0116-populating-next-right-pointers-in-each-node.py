"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue=deque([(root,0)])
        while queue:
            node,level=queue.popleft()
            if queue and queue[0][1] == level:
                node.next = queue[0][0]
            else:
                node.next = None
            if node.left is not None:
                queue.append([node.left,level+1])
            if node.right is not None:
                queue.append([node.right,level+1])
        return root