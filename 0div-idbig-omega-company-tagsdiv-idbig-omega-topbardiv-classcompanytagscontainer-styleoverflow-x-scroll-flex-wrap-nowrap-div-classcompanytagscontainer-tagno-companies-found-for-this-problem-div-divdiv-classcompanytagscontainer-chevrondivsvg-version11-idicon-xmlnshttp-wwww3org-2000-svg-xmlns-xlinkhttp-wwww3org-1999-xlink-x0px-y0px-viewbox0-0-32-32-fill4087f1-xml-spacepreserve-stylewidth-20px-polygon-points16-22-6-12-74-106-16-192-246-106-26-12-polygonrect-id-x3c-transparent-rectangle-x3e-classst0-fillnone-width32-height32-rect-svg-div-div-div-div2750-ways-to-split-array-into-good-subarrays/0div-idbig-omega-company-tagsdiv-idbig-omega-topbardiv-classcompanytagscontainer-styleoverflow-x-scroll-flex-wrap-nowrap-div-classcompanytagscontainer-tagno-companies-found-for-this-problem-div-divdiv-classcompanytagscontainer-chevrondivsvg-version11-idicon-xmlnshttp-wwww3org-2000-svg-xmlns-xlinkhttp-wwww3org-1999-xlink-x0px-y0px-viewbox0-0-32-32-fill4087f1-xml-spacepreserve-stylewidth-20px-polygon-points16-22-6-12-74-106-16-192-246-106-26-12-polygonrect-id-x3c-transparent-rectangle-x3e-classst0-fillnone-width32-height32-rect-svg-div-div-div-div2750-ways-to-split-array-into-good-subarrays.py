class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n =len(nums)
        MOD = int(1e9)+7
        dp =[[-1]*2 for _ in range(n)]
        def recur(idx,cnt):
            if idx==n:
                if cnt==1:
                    return 1
                return 0
            
            cnt += (nums[idx]==1)
            
            if cnt>1:
                return 0
            
            if dp[idx][cnt]!=-1:
                return dp[idx][cnt]
            
            
            take = recur(idx+1,cnt)
            nottake=0
            if cnt==1:
                nottake = recur(idx+1,0)
            
            dp[idx][cnt] =  (take+nottake)%MOD
            return dp[idx][cnt]
        
        val = recur(0,0)
        return val