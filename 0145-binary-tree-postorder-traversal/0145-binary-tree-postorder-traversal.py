# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ans=[]
        if not root:
            return ans
        
        
        def solve(root):
            if not root:
                return
            
            solve(root.left)
            solve(root.right)
            ans.append(root.val)
        
        solve(root)
        
        return ans
        
        
        