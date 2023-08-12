class Solution:
    def deleteString(self, s: str) -> int:
        n=len(s)    
        if len(set(s))==1:
            return n
    
        
        @cache
        def recur(i):
            if i==n:
                return 0
            
            ans = 1
            for l in range(1,n):
                if i+l<=n and i+2*l<=n:
                    if s[i:i+l]==s[i+l:i+2*l]:
                        ans = max(1+recur(i+l),ans)
                else:
                    break
            return ans
        
        val = recur(0)
            
        return val
                        
                