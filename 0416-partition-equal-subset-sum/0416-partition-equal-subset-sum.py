class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2!=0:
            return False
        target = summ//2
        
        dp=[[-1 for j in range(target+1)] for x in range(len(nums))]
        
        def recur(index,target):
            if target==0:
                return True
            if index==0:
                return nums[index]==target
            if dp[index][target]!=-1:
                return dp[index][target]
            nottake=recur(index-1,target)
            take=False
            if nums[index]<=target:
                take=recur(index-1,target-nums[index])
            
            dp[index][target] =  take or nottake
            return dp[index][target]
        
        return recur(len(nums)-1,target)
        
        