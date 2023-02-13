# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        longest=[0]
        
        def dfs(root):
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            
            if root.left and root.val==root.left.val:
                left+=1
            else:
                left=0
            
            if root.right and root.val == root.right.val:
                right+=1
            else:
                right=0
            
            longest[0]= max(longest[0],left+right)
            
            return max(left,right)
        dfs(root)
        
        return longest[0]
            
        

        