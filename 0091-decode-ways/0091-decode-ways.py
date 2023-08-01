class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        dp =[-1 for _ in range(n+10)]
        def recur(idx):
            if idx==n:
                return 1
            
            if dp[idx]!=-1:
                return dp[idx]
            
            
            
            
            ans = 0
            for i in range(idx,n+1):
                if 1<=int(s[idx:i+1])<=26 and s[idx]!="0":
                    ans+=recur(i+1)
            dp[idx] = ans
            return dp[idx]
        val = recur(0)
        return (val)