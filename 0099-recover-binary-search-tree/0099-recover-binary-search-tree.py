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
        self.first,self.sec,self.prev = None,None,None

        self.inOrder(root)
        self.first.val,self.sec.val = self.sec.val,self.first.val
        
    def inOrder(self,root):
        if not root:
            return

        self.inOrder(root.left)

        if self.prev:
            if self.prev.val>root.val:
                if not self.first:
                    self.first = self.prev
                self.sec = root 
        self.prev=root

        self.inOrder(root.right)


        
        