# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=deque()
        
        q.append([root,None,0])
        
        res=[]
        while q:
            if len(res)==2:
                break
                
            node,parent,depth = q.popleft()
            
            if node.val==x or node.val==y:
                res.append([parent,depth])
            
            if node.left:
                q.append([node.left, node, depth+1])
            
            if node.right:
                q.append([node.right, node, depth+1])
        
        node_x,node_y =res
        if node_x[0]!=node_y[0] and node_x[1]==node_y[1]:
            return True
        
        return False
            
            
        