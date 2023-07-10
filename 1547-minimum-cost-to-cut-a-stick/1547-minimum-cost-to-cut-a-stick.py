class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        dp={}
        
        def recur(l,r):
            if r-l==1:
                return 0
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            res=10**9
            for c in cuts:
                if l<c<r:       ## only make a cut if it is possible to do so
                    res=min(res, r-l+recur(l,c)+recur(c,r))
            
            dp[(l,r)]= res=0 if res==10**9 else res
            return dp[(l,r)]
        
        return recur(0,n)
                
                