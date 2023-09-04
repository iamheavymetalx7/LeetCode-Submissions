# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nmax = 10**5+1
        parent = [[0]*(nmax) for _ in range(21)]
        lvl = [0 for _ in range(nmax)]
        
        def dfs(src,par):
            if src is None:
                return
            
            if par is not None:
                lvl[src.val]=1+lvl[par.val]
            else:
                lvl[src.val] =0
            
            if par is not None:
                parent[0][src.val]=par.val
                
            for j in range(1,21):
                x = parent[j-1][src.val]
                if x is not None:
                    parent[j][src.val]=parent[j-1][x]
            
            if src.left:
                dfs(src.left,src)
            if src.right:
                dfs(src.right,src)
                
        dfs(root,None)
        
        # print(parent)
        # print(lvl)
        
        def LCA(u,v):
            if lvl[u]>lvl[v]:
                u,v=v,u
            
            diff = lvl[v]-lvl[u]
            
            for j in range(21):
                if diff&(1<<j):
                    v = parent[j][v]
            if u==v:
                return u
            
            for j in range(20,-1,-1):
                if parent[j][u]!=parent[j][v]:
                    u,v = parent[j][u],parent[j][v]
            
            return parent[0][u]
        
        ans = LCA(p.val,q.val)
        
        q=deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if node.val == ans:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
            
        