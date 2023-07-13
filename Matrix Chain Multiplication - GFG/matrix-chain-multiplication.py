#User function Template for python3
# from functools import cache
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        
        dp =[[0]*(N) for _ in range(N)]
        
        for i in range(N):
            dp[i][i] =0
            
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                mini = 10**9
                for k in range(i,j):
                    steps = arr[i-1]*arr[k]*arr[j]
                    steps+= dp[i][k]+dp[k+1][j]
                    
                    mini = min(mini,steps)
                dp[i][j] =mini
        return dp[1][N-1]
        
        # def f(i,j):
        #     if i==j:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
                
        #     mini = 10**9
        #     for k in range(i,j):
        #         steps = arr[i-1]*arr[k]*arr[j]
        #         steps+= f(i,k)+f(k+1,j)
                
        #         mini = min(mini,steps)
        #     dp[i][j] = mini
        #     return dp[i][j]
        
        # return f(1,N-1)
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends