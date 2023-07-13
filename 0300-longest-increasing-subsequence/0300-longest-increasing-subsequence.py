class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        
        
        temp=[]
        temp.append(nums[0])
        
        for i in range(1,n):
            # print(nums[i])
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                idx = bisect_left(temp,nums[i])
                # print(temp,idx,nums[i])
                temp[idx]=nums[i]
        
        return len(temp)
                
        
## Algorithmic
        
#         dp =[1]*(n)
#         for idx in range(n):
#             for prev in range(idx):
#                 if nums[prev]<nums[idx]:
#                     dp[idx]=max(1+dp[prev],dp[idx])
        
#         return max(dp)
        
        
        
## Tabulation:
        
#         dp=[[0]*(n+1) for _ in range(n+1)]
        
        
#         for ind in range(n-1,-1,-1):
#             for prev in range(ind-1,-2,-1):
#                 nottake = dp[ind+1][prev+1]
#                 take =0
#                 if prev==-1 or nums[ind]>nums[prev]:
#                     take = 1+dp[ind+1][ind+1] 
#                 dp[ind][prev+1] = max(take, nottake)

#         return dp[0][-1+1]

## Recurrence:

        
#         def f(i,prev):
#             if i==n:
#                 return 0
#             if dp[i][prev+1]!=-1:
#                 return dp[i][prev+1]
#             nottake = f(i+1,prev)
#             take =0
#             if prev==-1 or nums[i]>nums[prev]:
#                 take = 1+f(i+1,i)
            
#             dp[i][prev+1] = max(take, nottake)
            
#             return dp[i][prev+1]
#         return f(0,-1)
        