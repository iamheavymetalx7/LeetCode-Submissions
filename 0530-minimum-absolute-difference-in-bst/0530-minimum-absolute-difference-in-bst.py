# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:# Definition for a binary tree node.

        
        q=deque()
        q.append(root)
        arr=[]
        
        while q:
            front = q.popleft()
            
            arr.append(front.val)
            
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
        
        arr.sort()
        mini=10**9
        n=len(arr)
        
        for i in range(1,n):
            mini=min(mini, arr[i]-arr[i-1])
            
        return mini
            
            
                