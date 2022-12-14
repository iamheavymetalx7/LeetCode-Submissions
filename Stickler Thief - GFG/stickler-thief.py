#User function Template for python3

class Solution:  
    
    def recur(self,a,index,dp):
        if index==0:
            return a[index]
        if index<0:
            return 0
        
        if dp[index]!=-1:
            return dp[index]
            
            
        pick = self.recur(a,index-2,dp)+a[index]
        notpick = 0+self.recur(a,index-1,dp)
        
        dp[index]=max(pick,notpick)
        return dp[index]


    def FindMaxSum(self,a, n):
        
        dp=[-1 for i in range(n)]
        
        return self.recur(a,n-1,dp)
        

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends