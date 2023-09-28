class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.sort()
        cuts=[0]+cuts+[n]
        
        
        m = len(cuts)
        
        @cache
        def recur(i,j):
            if i>j:
                return 0
            
            mini = int(1e19)
            for k in range(i,j+1):
                ans =cuts[j+1]-cuts[i-1]+recur(i,k-1)+recur(k+1,j)
                mini = min(ans,mini)
            return mini
        val = recur(1,m-2)
        return val