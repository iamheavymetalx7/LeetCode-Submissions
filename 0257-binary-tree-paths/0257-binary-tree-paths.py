# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def helper(node,path):
            if node.left is None and node.right is None:
                
                ans.append(path+str(node.val))
            if node.left:
                helper(node.left, path+str(node.val)+"->")
            if node.right:
                helper(node.right, path+str(node.val)+"->")
        helper(root,"")
        return (ans)
        
        