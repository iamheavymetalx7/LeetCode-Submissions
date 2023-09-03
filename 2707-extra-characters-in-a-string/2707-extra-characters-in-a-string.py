class Solution:
    def minExtraChar(self, s: str, dic: List[str]) -> int:
        
        n=len(s)
        dictt = set()
        
        for ele in dic:
            dictt.add(ele)
        
        @cache
        def recur(idx):
            if idx>=n:
                return 0
            
            
            ans =int(1e19)
            for nidx in range(idx+1,n+1):
                t = s[idx:nidx]
                
                if t in dictt:
                    ans=min(ans,recur(nidx))
            ans = min(ans,1+recur(idx+1))
            
            return ans
        
        val = recur(0)
        return val