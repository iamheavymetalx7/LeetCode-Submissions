class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(string):
            return string==string[::-1]

        n=len(s)
        dp=[-1]*(n)
        INF = 10**9
        def recur(idx):
            if idx==n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            ans=INF
            for j in range(idx,n):
                if isPalindrome(s[idx:j+1]):
                    ans=min(ans,1+recur(j+1))
            
            dp[idx]=ans
            return dp[idx]
        return recur(0)-1