# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first,middle,last =[None]*(3)
        prev = TreeNode(-int(1e18))
        
        
        def dfs(node):
            nonlocal first,prev,last,middle
            if not node:
                return
            
            dfs(node.left)
            
            if prev is not None and (prev.val > node.val):
                if first is None:
                    first = prev
                    middle = node
            
                else:
                    last = node
                    
            prev=node
            
            dfs(node.right)
        
        dfs(root)
        
        if (first and last):
            first.val,last.val = last.val,first.val
        elif (first and middle):
            first.val,middle.val = middle.val, first.val
                