# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        
        q.append((root,0))
        ans=[]

        
        while q:
            a=[]
            for _ in range(len(q)):
                node,lvl = q.popleft()

                a.append(node.val)            
                if node.left:
                    q.append((node.left,lvl+1))

                if node.right:
                    q.append((node.right,lvl+1))
            ans.append(a)
            
        maxi=-float('inf')
        idx=0
        
        # print(ans)
        for i,x in enumerate(ans):
            if maxi<sum(x):
                maxi = sum(x)
                idx=i
        return idx+1
        