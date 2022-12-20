# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global MaxSum
        MaxSum =-math.inf
        
        def dfs(node):
            global MaxSum
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left=max(left,0)
            right=max(right,0)
            
            MaxSum = max(MaxSum,node.val+left+right)
        
            return node.val + max(left,right)
            
        dfs(root)
        return MaxSum
            
        