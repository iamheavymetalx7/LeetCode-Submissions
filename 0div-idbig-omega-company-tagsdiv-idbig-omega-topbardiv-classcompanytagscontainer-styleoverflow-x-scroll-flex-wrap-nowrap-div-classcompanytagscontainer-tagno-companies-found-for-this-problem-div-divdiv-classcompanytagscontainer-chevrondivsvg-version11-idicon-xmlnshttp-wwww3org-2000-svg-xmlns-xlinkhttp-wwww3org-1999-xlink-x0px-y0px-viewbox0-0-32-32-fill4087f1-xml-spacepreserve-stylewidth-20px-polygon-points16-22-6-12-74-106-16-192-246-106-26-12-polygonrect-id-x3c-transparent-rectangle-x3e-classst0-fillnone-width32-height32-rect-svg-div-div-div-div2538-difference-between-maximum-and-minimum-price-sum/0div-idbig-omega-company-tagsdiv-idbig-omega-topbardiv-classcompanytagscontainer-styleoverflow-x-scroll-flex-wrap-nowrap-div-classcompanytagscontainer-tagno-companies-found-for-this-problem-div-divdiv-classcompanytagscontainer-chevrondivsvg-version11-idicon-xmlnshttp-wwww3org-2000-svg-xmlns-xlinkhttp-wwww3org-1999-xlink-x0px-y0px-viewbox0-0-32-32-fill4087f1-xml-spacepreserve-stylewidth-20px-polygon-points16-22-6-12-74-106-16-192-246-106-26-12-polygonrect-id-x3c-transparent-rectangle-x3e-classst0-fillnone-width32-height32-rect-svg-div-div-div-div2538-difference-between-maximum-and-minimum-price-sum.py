'''
https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/discuss/3052596/Re-rooting-or-O(N)-or-Explained
'''

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g =[[] for _ in range(n)]
        
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
        max_in =[0 for _ in range(n)]
        
        
        def dfs_in(src,par):
            res =0
            
            for child in g[src]:
                if child==par:
                    continue
                
                res = max(res,dfs_in(child,src))
            res+=price[src]
            max_in[src]=res
            
            return max_in[src]
        dfs_in(0,-1)
        # print(max_in,"thisss")
        
        
        max_dif =[0]
        
        def dfs_out(src,par,par_contribution):
            # print(src,par,par_contribution,"recurrence")
            c1=-1
            mc1,mc2=0,0
            
            for child in g[src]:
                if child == par:
                    continue
                
                if max_in[child]>mc1:
                    mc2=mc1
                    c1=child
                    mc1= max_in[child]
                elif max_in[child]>mc2:
                    mc2=max_in[child]
            # print(c1,/mc1,mc2,par_contribution)
            path1 = mc1
            path2 = par_contribution
            
            max_dif[0]=max(max_dif[0],path1,path2)
            
            for child in g[src]:
                if child == par:
                    continue
                if c1==child:
                    dfs_out(child,src,price[src]+max(mc2,par_contribution))
                else:
                    dfs_out(child,src,price[src]+max(mc1,par_contribution))
        
        dfs_out(0,-1,0)
        
        return max_dif[0]
            

            
        