import math
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        
        dp =[int(1e8)]*n
        
        def recur(index):
            if index>=n-1:
                return 0
            
            if dp[index]!=int(1e8):
                return dp[index]
            
            for j in range(1,1+nums[index]):
                dp[index] = min(1+recur(index+j),dp[index])

            return dp[index]
        
        return recur(0)
        
        