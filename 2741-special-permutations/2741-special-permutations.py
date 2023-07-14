class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n=len(nums)
        MOD = 10**9+7
        dp=[[-1]*(1<<14) for _ in range(14)]
        
        def CountPerm(last_ind,mask):
            if mask == (1<<n)-1:
                return 1
            
            if dp[last_ind][mask]!=-1:
                return dp[last_ind][mask]
            
            ans=0
            for cur in range(0,n):
                is_taken = (mask & (1<<cur))>0
                if is_taken:continue
                
                
                if (mask==0 or nums[last_ind]%nums[cur]==0 or nums[cur]%nums[last_ind]==0):
                    ans = ans + CountPerm(cur, mask | (1<<cur)) % MOD
                    
            dp[last_ind][mask]=ans
            return dp[last_ind][mask]
        
        return CountPerm(0,0)%MOD
                
            
            