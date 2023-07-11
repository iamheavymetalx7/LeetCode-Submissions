#User function Template for python3
import sys
sys.setrecursionlimit(10**8)

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        dp=[[-1]*(W+1) for _ in range(N)]
        
        def f(idx,W):
            if idx==0:
                if wt[idx]<=W:
                    return val[0]*(W//wt[idx])
                else:
                    return 0
            
            if dp[idx][W]!=-1:
                return dp[idx][W]
            
            take  =0
            
            nottake = f(idx-1,W)
            if wt[idx]<=W:
                take = val[idx]+f(idx,W-wt[idx])
            
            dp[idx][W] = max(take, nottake)

            return dp[idx][W]
        
        return f(N-1,W)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends