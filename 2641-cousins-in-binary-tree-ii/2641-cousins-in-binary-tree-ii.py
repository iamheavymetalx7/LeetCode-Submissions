# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        sums=defaultdict(int)

        q=[(root,0)]

        while q:
            node,d=q.pop()

            sums[d]+=node.val

            if node.left:
                q.append((node.left, d+1))

            if node.right:
                q.append((node.right, d+1))
        
        
        q=[(root,root.val if root else 0,0,0)]
        
        while q:
            
            node,node_val,others,d=q.pop()
            
            node.val = sums[d]-node_val-others
            
            if node.left:
                q.append((node.left, node.left.val, node.right.val if node.right else 0,d+1))
            if node.right:
                q.append((node.right, node.right.val, node.left.val if node.left else 0,d+1))
        
        return root
        