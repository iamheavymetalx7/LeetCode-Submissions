# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left mid right
        if not root:
            return []
        
        ans=[]
        
        def helper(node):
            if node.left:
                helper(node.left)
                
            ans.append(node.val)
            
            if node.right:
                helper(node.right)
        helper(root)
        return ans