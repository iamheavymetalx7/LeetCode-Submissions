# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mindepth =0
        
        q=deque()
        if not root:
            return mindepth
        q.append(root)

        while q:
            t=len(q)
            mindepth+=1

            for i in range(t):
                front=q.popleft()
                
                if not front.left and not front.right:
                    return mindepth
                
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
        
        