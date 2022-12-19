# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag=0
        ans=[]
        if not root:
            return []
        
        q=deque()
        q.append(root)
        
        while q:
            t=len(q)
            arr=[]
            flag+=1
            for i in range(t):
                front=q.popleft()
                arr.append(front.val)
                
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            if flag%2:
                ans.append(arr)
            else:
                ans.append(arr[::-1])
        return ans
            