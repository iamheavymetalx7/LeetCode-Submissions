#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        
        
        # def recur(index,w):
            
        #     if index==0:
        #         if wt[0]<=w:
        #             return val[0]
        #         return 0
                
                
            
            
        #     if dp[index][w]!=-1:
        #         return dp[index][w]
            
            
        #     notpick = recur(index-1,w)
        #     pick = 0
        #     if wt[index]<=w:
        #         pick = val[index]+recur(index-1,w-wt[index])
            
        #     dp[index][w] = max(pick, notpick)
        #     return dp[index][w]
        # return recur(n-1,W)
        dp=[[0]*(W+1) for _ in range(n)]

        for w in range(wt[0],W+1):
            
            dp[0][w]=val[0] 
        
        for index in range(1,n):
            for w in range(W+1):
                
            
                notpick = dp[index-1][w]
                pick = 0
                if wt[index]<=w:
                    pick = val[index]+dp[index-1][w-wt[index]]
                
                dp[index][w] = max(pick, notpick)
        
        
        # print(dp)
        return dp[n-1][W]
        
        

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