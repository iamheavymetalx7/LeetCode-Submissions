import math
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[0]*(n+1) for j in range(n+1)]
        
        for index in range(n-1,-1,-1):
            for prev_index in range(index-1,-2,-1):

                length = dp[index+1][prev_index+1]        ##not take

                if prev_index == -1 or nums[index]>nums[prev_index]:
                    length=max(length, 1+dp[index+1][index+1])  ##take

                dp[index][prev_index+1] =length
        return dp[0][-1+1]   
        
        
        
        
#         def recur(index,prev_index):
#             if index>=n:
#                 return 0
#             if dp[index][prev_index+1]!=-1:
#                 return dp[index][prev_index+1]
#             length = recur(index+1, prev_index)        ##not take
            
#             if prev_index == -1 or nums[index]>nums[prev_index]:
#                 length=max(length, 1+recur(index+1,index))  ##take
            
#             dp[index][prev_index+1] =length
#             return dp[index][prev_index+1]
   
                
        
