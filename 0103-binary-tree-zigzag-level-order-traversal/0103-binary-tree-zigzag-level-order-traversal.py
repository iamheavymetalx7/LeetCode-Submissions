# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if not root:
            return []
        
        q.append(root)
        ans=[]
        val=0
        while q:
            n=len(q)
            val+=1
            arr=[]
            for _ in range(n):
                node = q.popleft()
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if val%2:
                ans.append(arr)
            else:
                ans.append(arr[::-1])
        
        return ans
                
            
            
        
        