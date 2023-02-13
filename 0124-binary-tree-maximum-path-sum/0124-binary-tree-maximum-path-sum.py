# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res=[-10**9]
        
        def dfs(root):
            if not root:
                # print("return as not node")
                return 0
            # print("go left..")
            left=dfs(root.left)
            # print("go right..")
            right=dfs(root.right)
            
            left=max(left,0)
            # print(left,"left...")
            right=max(right,0)
            # print(right,"right...")
            
            
            res[0]=max(res[0],left+right+root.val)
            # print("return to prev node with val:", root.val+max(left,right))
            return root.val+max(left, right)
        
        dfs(root)
        return res[0]