# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        q= deque()
        mind=0
        if not root:
            return mind
        
        q.append(root)

        while q:
            r = len(q)

            mind+=1
            
            for _ in range(r):
                node = q.popleft()
            
                if not node.left and not node.right:
                    return mind

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            
        
        