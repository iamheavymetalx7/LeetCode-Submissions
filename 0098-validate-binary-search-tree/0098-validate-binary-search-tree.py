'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        plus_inf=float('inf')
        min_inf=-float('inf')
        
        def helper(node, maxi, mini):
            if mini<node.val<maxi:
                if node.left:
                    helper(node.left,node.val,mini)
                if node.right:
                    helper(node.right,maxi,node.val)
            else:
                self.flag=0
                return self.flag
            
            return self.flag
        
        return(helper(root,plus_inf,min_inf))
'''

##Second Approach:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def solve(self, root, mini, maxi):
        if not root:
            return True
        if(root.val<=mini or root.val>=maxi):
            return False
        return self.solve(root.left, mini, root.val) and self.solve(root.right,root.val,maxi)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root, -float('inf'), float('inf'))
        

        
        
        
        