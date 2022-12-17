import math
class Solution:
    
    def isPalindrome(self,s):
        return s==s[::-1]

    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[-1]*n
        def recur(index,n):
            if index==n:
                return 0
            if dp[index]!=-1:
                return dp[index]
            mini=math.inf
            for j in range(index,n):
                if self.isPalindrome(s[index:j+1]):
                    cnt = 1+recur(j+1,n)
                    mini=min(cnt,mini)
                
            dp[index] = mini
            return dp[index]
        return recur(0,n)-1
                    