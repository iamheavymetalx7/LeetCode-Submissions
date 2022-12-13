#User function Template for python3

class Solution:
    def recursion(self,W,wt,val,n,dic,i):
        if i>=len(wt) or W<=0:
            return 0
        if (W,i) not in dic:
            if wt[i]>W:
                dic[(W,i)] = self.recursion(W,wt,val,n,dic,i+1)
            else:
                take = val[i]+self.recursion(W-wt[i],wt,val,n,dic,i+1)
                not_take = self.recursion(W,wt,val,n,dic,i+1)
                dic[(W,i)] =max(take,not_take)
        return dic[(W,i)]
        
        
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        return self.recursion(W,wt,val,n,{},0)
        
       
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