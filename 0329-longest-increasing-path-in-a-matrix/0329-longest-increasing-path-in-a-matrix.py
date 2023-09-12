class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        dp =[[1]*(m) for _ in range(n)]
        
        dire=[(1,0),(0,1),(-1,0),(0,-1)]
        ans = 1
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append([matrix[i][j],i,j])
        
        arr.sort(reverse=True)
        
        
        for x in range(len(arr)):
            _,i,j = arr[x]
            f=False
            val=0
            for dx,dy in dire:
                dx+=i
                dy+=j

                if 0<=dx<n and 0<=dy<m and matrix[dx][dy]>matrix[i][j]:

                    val = max(dp[dx][dy],val)
                    # print(i,j,dx,dy,val,"ehehe")

                    f=True
            if f:
                # print(i,j,dp[i][j]+val,dp[i][j])
                dp[i][j]+=val
                ans=max(ans,dp[i][j])
            
                    
                        

        # print(dp)
        return ans