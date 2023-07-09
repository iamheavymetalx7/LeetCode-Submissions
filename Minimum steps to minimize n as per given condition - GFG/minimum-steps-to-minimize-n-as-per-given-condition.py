#User function Template for python3
class Solution:
	def minSteps(self, N):
	    
	    dp=[0 for _ in range(10**4+1)]
	    
	    dp[1]=0
	    dp[2]=1
	    dp[3]=1
	    
	    i=4
	    
	    while i<=N:
	        if i%2==0 and i%3==0:
	            dp[i]=min(dp[i//2]+1,1+dp[i-1],dp[i//3]+1)
	        elif i%2==0:
	           dp[i]=min(dp[i//2]+1,dp[i-1]+1)
            elif i%3==0:
                dp[i]=min(dp[i//3]+1,dp[i-1]+1)
            else:
                dp[i]=dp[i-1]+1
        
            i+=1
        return dp[N]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.minSteps(N)
		print(ans)

# } Driver Code Ends