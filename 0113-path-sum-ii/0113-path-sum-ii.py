# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        
        if not root:
            return []
        
        def helper(node,targetSum,arr):
            if not node.left and not node.right and targetSum==node.val:
                arr.append(node.val)
                ans.append(arr)
                
            if node.left:
                helper(node.left,targetSum-node.val,arr+[node.val])
            
            if node.right:
                helper(node.right, targetSum-node.val,arr+[node.val])
        helper(root,targetSum,[])
        return ans