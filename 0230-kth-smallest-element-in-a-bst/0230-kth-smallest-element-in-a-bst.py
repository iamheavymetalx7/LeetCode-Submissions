# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## post order traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[0]
        def dfs(node):
            nonlocal k
            if node is None:
                return
            dfs(node.left)
            k-=1
            if k==0:
                res[0] = node.val
            
            dfs(node.right)
        
        dfs(root)
        return res[0]