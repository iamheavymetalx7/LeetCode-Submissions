# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        inorder =[]
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        dfs(root)
        
        inorder.sort()
        
        i=0
        
        def dfs(node):
            nonlocal i
            if not node:
                return
            dfs(node.left)
            print(inorder[i],node.val)
            if inorder[i]!=node.val:
                node.val = inorder[i]
            i+=1
            dfs(node.right)
        dfs(root)