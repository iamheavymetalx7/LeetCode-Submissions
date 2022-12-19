# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        ans=[]
        if not root:
            return [0]
        q.append(root)
        while q:
            t=len(q)
            arr=[]
            for i in range(t):
                front = q.popleft()
                arr.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
                
            ans.append(sum(arr)/len(arr))
        return ans