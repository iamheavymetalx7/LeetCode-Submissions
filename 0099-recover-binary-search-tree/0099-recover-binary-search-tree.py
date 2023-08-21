# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## now in O(1) space

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        first,sec,prev = [None]*(3)
        
        def inOrder(root):
            nonlocal first,sec,prev
            if not root:
                return
            
            inOrder(root.left)
            
            if prev:
                if prev.val>root.val:
                    if not first:
                        first = prev
                    sec = root 
            prev=root
            
            inOrder(root.right)
        
        inOrder(root)
        first.val,sec.val = sec.val,first.val
        
        