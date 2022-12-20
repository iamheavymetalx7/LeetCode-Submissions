# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def helper(node,string):
            if node.left is None and node.right is None:
                string+=str(node.val)
                ans.append(string)
            
            if node.left:
                helper(node.left,string+str(node.val))
            
            if node.right:
                helper(node.right,string+str(node.val))
        helper(root, "")
        
        summ=0
        for i in range(len(ans)):
            summ+=int(ans[i])
        
        return summ