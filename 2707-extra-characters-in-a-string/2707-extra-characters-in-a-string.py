class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        n=len(s)
        
        dic = set()
        
        for ele in dictionary:
            dic.add(ele)
        
        dp=[-1]*(n+1)
        
        def recur(idx):
            if idx>=n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            res = int(1e9)
            # print(idx,"recur")
            
            for nidx in range(idx+1,n+1):
                # print("inside for",nidx,s[idx:nidx])
                t = s[idx:nidx]
                if t in dic:
                    res = min(res,recur(nidx))
            
            res = min(res, 1+recur(idx+1))

            dp[idx]=res
            
            return dp[idx]
        
        ans = recur(0)
        # print(dp)
        
        return ans