# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr=[]
        def dfs(node,s):
            nonlocal arr

            s+=str(node.val)
            if (not node.left) and (not node.right):
                arr+=[s]
                
            if node.left:
                dfs(node.left,s)

            if node.right:
                dfs(node.right,s)
        dfs(root,"")
        
        summ=0
        for ele in arr:
            summ+=int(ele)
            
        return summ
                
        