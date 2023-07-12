#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here

        dp =[[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=0
            
        for j in range(m+1):
            dp[0][j]=0
        
        maxi =0
        
        for i1 in range(1,n+1):
            for i2 in range(1,m+1):
                
                if S1[i1-1]==S2[i2-1]:
                    dp[i1][i2] = 1+dp[i1-1][i2-1]
                    maxi=max(maxi, dp[i1][i2])
                else:
                    dp[i1][i2] =0
        
        return maxi
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends