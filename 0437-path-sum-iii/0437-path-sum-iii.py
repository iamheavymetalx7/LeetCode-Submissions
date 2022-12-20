# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        global result
        result =0
        
        def dfs(node):
            if node is None:
                return 
            
            find_path(node,targetSum)
            dfs(node.left)
            dfs(node.right)
        
        def find_path(node,targetSum):
            global result
            if node is None:
                return 0
            if targetSum == node.val:
                result+=1
            
            find_path(node.left, targetSum-node.val)
            find_path(node.right, targetSum-node.val)
        
        dfs(root)
    
        return result
                
        