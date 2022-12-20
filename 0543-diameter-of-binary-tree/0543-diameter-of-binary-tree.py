# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global dia
        dia =0
        
        def helper(node):
            global dia
            if not node:
                return -1
            
            left = helper(node.left)
            right = helper(node.right)
            
            dia=max(dia,left+right+2)
            
            return 1+max(left,right)
        
        helper(root)
        return dia
        