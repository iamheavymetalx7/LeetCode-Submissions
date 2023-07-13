#User function Template for python3
# from functools import cache
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        
        dp =[[-1]*(N) for _ in range(N)]
        def f(i,j):
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
                
            mini = 10**9
            for k in range(i,j):
                steps = arr[i-1]*arr[k]*arr[j]
                steps+= f(i,k)+f(k+1,j)
                
                mini = min(mini,steps)
            dp[i][j] = mini
            return dp[i][j]
        
        return f(1,N-1)
                
                

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