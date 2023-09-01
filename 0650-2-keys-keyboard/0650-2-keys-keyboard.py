class Solution:
    def minSteps(self, n: int) -> int:
        inf = int(1e19)
        if n==1:
            return 0
        
        ## initially we have one character
        # recur(x,prev) -> current length, len of prev copied element
        @cache
        def recur(x,prev):
            if x>=n:
                if x==n:
                    return 0
                return inf
            
            paste = 1+recur(x+prev,prev)
            copy = 2+recur(2*x,x)
            
            ops = min(copy,paste)
            
            return ops
            
        
        val = recur(1,1)
            
        return val+1