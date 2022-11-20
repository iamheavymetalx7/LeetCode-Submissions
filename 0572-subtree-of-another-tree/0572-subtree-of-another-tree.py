# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=0
    def helper(self,node1, node2):
        if node1 is None or node2 is None:
            return node1 is None and node2 is None
        
        return node1.val==node2.val and self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        elif self.helper(root,subroot):
            return True
        
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right,subroot)
        
     