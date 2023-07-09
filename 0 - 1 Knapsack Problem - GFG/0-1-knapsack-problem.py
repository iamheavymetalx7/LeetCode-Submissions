#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        dp=[[-1]*(W+1) for _ in range(n+1)]

        def recur(index,W):
            if index>=n or W<0:
                return 0
                
            if dp[index][W]!=-1:
                return dp[index][W]
            
            take=0
            if wt[index]<=W:
                take = val[index]+recur(index+1, W-wt[index])
            
            nottake = recur(index+1, W)
            
            dp[index][W]=max(take,nottake)
            
            return dp[index][W]
        
        return recur(0,W)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends