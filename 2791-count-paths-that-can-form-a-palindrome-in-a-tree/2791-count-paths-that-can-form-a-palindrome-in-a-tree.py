class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g =[[] for _ in range(n)]
        
        for j in range(1,n):
            g[parent[j]].append([j,s[j]])
        
        
        freq = defaultdict(int)
        
        
        def dfs(node,path):
            freq[path]+=1
            
            for adj in g[node]:
                ch = ord(adj[1])-ord('a')
                # print(adj[1],node,ch)
            
                path^=1<<ch
                dfs(adj[0],path)
                path^=1<<ch
            
        
        dfs(0,0)
        
        res =0
        
        for val,cnt in freq.items():
            
            for j in range(26):
                other = val^(1<<j)
                
                if other in freq:
                    res+=cnt*freq[other]
            res+=cnt*(cnt-1)
        return res//2
                    