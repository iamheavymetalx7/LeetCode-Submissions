class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        dp=[-1]*(n)
        
        def recur(index):
            if index>=n:
                return 0
            
            if dp[index]!=-1:
                return dp[index]
            
            dp[index]=max(recur(index+2)+nums[index],recur(index+1))
            
            return dp[index]
        
        return recur(0)