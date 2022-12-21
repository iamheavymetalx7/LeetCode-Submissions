class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*len(nums)
        
        def recur(index):
            if index>=n:
                return 0
            
            if dp[index]!=-1:
                return dp[index]
        
            take= recur(index+2)+nums[index]
            nottake = recur(index+1)
            
            dp[index]=max(take,nottake)
            
            return dp[index]
        return recur(0)
            