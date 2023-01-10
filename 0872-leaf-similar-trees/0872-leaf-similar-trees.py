# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Think of DFS traversal with in-order.
In-order DFS's traversal rule (left node, current node, right node) naturally fits this demand.

Based on in-order DFS and leaf node checking, we can build a algorithm to trace leaf sequence, then compare equality to get the result.
'''

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_seq1=[]
        leaf_seq2=[]
        
        def helper( node, arr):
            if node.left:
                helper(node.left,arr)
                
            if not node.left and not node.right:
                arr.append(node.val)
            
            if node.right:
                helper(node.right,arr)
                
        helper(root1,leaf_seq1)
        helper(root2,leaf_seq2)
        
        
        
        return leaf_seq1==leaf_seq2