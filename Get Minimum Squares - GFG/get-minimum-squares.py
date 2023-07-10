#User function Template for python3
import math
class Solution:
	def MinSquares(self, n):
        
        dp=[0,1,2,3]
        
        for i in range(4,n+1):
            dp.append(i)
            
            for x in range(1,int(math.sqrt(i))+1):
                temp = x*x
                if x>i:
                    break
                
                else:
                    dp[i] =min(dp[i], dp[i-temp]+1)


        return dp[n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

from math import ceil, sqrt
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.MinSquares(n)
		print(ans)
# } Driver Code Ends