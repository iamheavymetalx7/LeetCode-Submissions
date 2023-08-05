'''
https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
'''

class Solution:
    def numTrees(self, n: int) -> int:
        
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]