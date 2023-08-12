class Solution:
    def deleteString(self, s: str) -> int:
        n=len(s)    
        if len(set(s))==1:
            return n
    
        # print(s,"start")
        
        @cache
        def recur(i):
            if i==n:
                return 0
            
            ans = 1
            for l in range(1,len(s[i:])):
                if i+l<=n and i+2*l<=n:
                    # print(s[i:i+l],s[i+l:i+2*l],s[i+l:])
                    if s[i:i+l]==s[i+l:i+2*l]:
                        ans = max(1+recur(i+l),ans)
                else:
                    break
            return ans
        
        val = recur(0)
            
        return val
                        
                