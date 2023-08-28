class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        
        n=len(nums)
        ss=sum(nums)
        if ss%k!=0:
            return False
        
        subsetVal = ss//k
        
        dp =[-1 for _ in range((1<<n)-1)]
        
        
        def recur(k,mask,curSum):
            if k==0:
                return mask==(1<<n)-1
            
            if curSum == subsetVal:
                return recur(k-1,mask,0)
            
            if dp[mask]!=-1:
                return dp[mask]
            
            ans = False
            
            for i in range(n):
                if (mask)&(1<<i):   # if this index is previously used, skip it
                    continue
                
                if curSum+nums[i]<=subsetVal:   # we take element only if it is less than overall subset sum
                    ans |= recur(k,mask^(1<<i),curSum+nums[i])      

            
            dp[mask]=ans
            return ans
        return recur(k,0,0)
        
        

        