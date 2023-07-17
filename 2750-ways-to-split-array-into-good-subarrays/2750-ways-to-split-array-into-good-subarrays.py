'''
https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/discuss/3679975/DP-Pick-and-Not-Pick-or-Explained-Handwritten-Fully-with-Dry-Run-or-O(N)-Time

'''

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        
        MOD=10**9+7
        
        dp=[[-1]*(2) for _ in range(n)]
        def recur(idx,cnt):
            if idx==n:
                if cnt==1:
                    return 1
                return 0
            
            if nums[idx]==1:
                cnt+=1
                
            if cnt>1:return 0
            
            if dp[idx][cnt]!=-1:
                return dp[idx][cnt]
            
            pick = recur(idx+1,cnt)         # pick = no split,cnt remains same
            notpick =0 
            if cnt==1:
                notpick = recur(idx+1,0)    # not pick, means split, so cnt goes to zero    
                
                
            
            

            dp[idx][cnt]=(pick+notpick)%MOD
            return dp[idx][cnt]
        return recur(0,0)
        
        
            
            
            