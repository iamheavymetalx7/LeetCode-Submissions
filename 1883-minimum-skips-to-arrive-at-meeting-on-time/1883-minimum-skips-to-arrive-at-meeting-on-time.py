from math import *
class Solution:
    def minSkips(self, dist: List[int], speed: int, target: int) -> int:
        if sum(dist)/speed>target:
            return -1
        
        n=len(dist)
        e=1e-9
        inf = int(1e19)
        
        @cache
        def recur(i,skips):
            if i>=n:
                return 0
            if skips<0:
                return inf
            
            
            return dist[i]/speed + min(recur(i+1,skips-1), ceil(recur(i+1,skips)-e))
        
        l=-1
        r=n
            
        while r-l>1:
            mid = (l+r)//2
            
            if recur(0,mid)-e<=target:
                r=mid
            else:
                l=mid
        return r