# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parent = dict()
        level=dict()
        
        def jumpParent(node,dist):
            while dist>0:
                node=parent[node]
                dist-=1
            return node
        
        def dfs(u,p,depth):
            if not u:
                return
            parent[u]=p
            level[u]=depth
            
            dfs(u.left,u,depth+1)
            dfs(u.right,u,depth+1)
        
        dfs(root,None,0)
        
        
        if level[p]<level[q]:
            q = jumpParent(q,level[q]-level[p])
        else:
            p = jumpParent(p,level[p]-level[q])
        
        while p!=q: ## jump until LCA
            q = parent[q]
            p = parent[p]
        
        return p
            