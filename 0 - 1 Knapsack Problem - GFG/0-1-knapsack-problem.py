#User function Template for python3
'''



class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knap2(self,W,wt,val,i,DP):
        if W<=0 or i>=len(wt):
            return 0
        if (W,i) not in DP:
            if wt[i]>W:
                DP[(W,i)] = self.knap2(W,wt,val,i+1,DP)
            else:
                DP[(W,i)]=max(val[i]+self.knap2(W-wt[i],wt,val,i+1,DP),self.knap2(W,wt,val,i+1,DP))
        return DP[(W,i)]
        

    

    def knapSack(self,W, wt, val, n):
        return self.knap2(W,wt,val,0,{})

        # code here


'''
class Solution:
    def recursion(self,W,wt,val,i,dp):
        if i>=len(wt) or W<=0:
            return 0
        if dp[i][W]!=-1:
            return dp[i][W]
        profit1=0
        if wt[i]<=W:
            profit1=val[i]+self.recursion(W-wt[i],wt,val,i+1,dp)
        profit2=self.recursion(W,wt,val,i+1,dp)
        
        dp[i][W]=max(profit1,profit2)
        return dp[i][W]
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[-1 for x in range(W+1)]for y in range(len(val))]
        
        return self.recursion(W,wt,val,0,dp)
        # code here


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