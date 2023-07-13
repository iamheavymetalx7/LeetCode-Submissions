class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)

        nums =[1]+nums+[1]
        
        dp=[[0]*(n+2) for _ in range(n+2)]
        
        
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                res= 0
                for k in range(i,j+1):
                    ans = nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j]
                    res=max(ans,res)
                dp[i][j]=res          
                
        return dp[1][n]
        
#         def recur(i,j):
#             if i>j:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             res= 0
#             for k in range(i,j+1):
#                 ans = nums[i-1]*nums[k]*nums[j+1]+recur(i,k-1)+recur(k+1,j)
#                 res=max(ans,res)
#             dp[i][j]=res
            
#             return dp[i][j]
#         return recur(1,n)