"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q=deque()
        if not root:
            return

        q.append(root)
        
        while q:
            t=len(q)
            while t>0:
                node = q.popleft()
                
                if t>1:
                    node.next=q[0]
                t-=1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root