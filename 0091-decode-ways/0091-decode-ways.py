from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n =len(s)
        
        @cache
        def recur(idx):
            if idx==n:
                return 1

            
            
            ans = 0
            for i in range(idx,n+1):
                if 1<=int(s[idx:i+1])<=26 and s[idx]!="0":
                    ans+=recur(i+1)

            return ans
        val = recur(0)
        return (val)