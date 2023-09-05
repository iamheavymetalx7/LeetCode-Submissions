# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def solve(root,cam,parcam):
            if root is None:
                if cam:
                    return inf
                return 0
            if root.left is None and root.right is None:
                if cam:
                    return 1
                if parcam:
                    return 0
                return inf
            
            ans=0
            if cam:
                return 1+min(solve(root.left,0,1),solve(root.left,1,1))+min(solve(root.right,0,1),solve(root.right,1,1))
        
            elif parcam:
                return min(solve(root.left,0,0),solve(root.left,1,0))+min(solve(root.right,0,0),solve(root.right,1,0))
            
            else:
                op1 = solve(root.left,1,0)+min(solve(root.right,0,0),solve(root.right,1,0))
                op2 = solve(root.right,1,0)+min(solve(root.left,0,0),solve(root.left,1,0))
                return min(op1,op2)
        
        
        
        return min(solve(root,1,0), solve(root,0,0))