from math import ceil
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        
        if sum(dist)/speed>hoursBefore:
            return -1
        
        n=len(dist)
        inf = int(1e19)
        e=1e-9
        
        
        def recur(i,skips):
            if i>=n:
                return 0
            if skips<0:
                return inf
            
            if dp[i][skips]!=-1:
                return dp[i][skips]
            
            dp[i][skips]  = dist[i]/speed+min(recur(i+1,skips-1),ceil(recur(i+1,skips)-e))
            return dp[i][skips]
        
        l=-1;r=n
        
        while r-l>1:
            mid = (l+r)//2
            dp=[[-1]*(mid+1) for _ in range(n+1)]
            if recur(0,mid)-e<=hoursBefore:
                r=mid
            else:
                l=mid
        return r