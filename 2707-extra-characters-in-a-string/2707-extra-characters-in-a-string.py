class Solution:
    def minExtraChar(self, s: str, dic: List[str]) -> int:
        
        n=len(s)
        
    
        @cache
        def recur(idx):
            if idx>=n:
                return 0
            
            
            ans =int(1e19)
            for ele in dic:
                m=len(ele)
                if s[idx:min(idx+m,n)]==ele:
                    ans = min(ans,recur(idx+m))
            ans=min(ans,1+recur(idx+1))
            return ans
        
        val = recur(0)
        return val