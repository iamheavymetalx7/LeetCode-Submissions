class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ=sum(nums)
        n=len(nums)
        
        k = (summ-target)
        
        if k%2 or k<0:
            return 0
        
        reqd = k//2
        
        
        dp=[[-1]*(reqd+1) for _ in range(n) ]
        
        
        
        
        def f(idx,tar):
            if idx==0:
                if nums[0]==0 and tar==0:
                    return 2
                if tar==0 or tar==nums[0]:
                    return 1
                return 0
             
            if dp[idx][tar]!=-1:
                return dp[idx][tar]
            
            
            notpick = f(idx-1,tar)
            pick=0
            if nums[idx]<=tar:
                pick = f(idx-1,tar-nums[idx])
            
            dp[idx][tar] = notpick+pick
            return dp[idx][tar]
        return f(n-1,reqd)
            
                 
                
        