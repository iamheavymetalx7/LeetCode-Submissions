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
            node = q.popleft()
            
            arr.append(node.val)
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        arr.sort()
        n=len(arr)
        mini=int(1e19)
        for i in range(1,n):
            mini=min(mini,arr[i]-arr[i-1])
        
        return mini
            
            
                