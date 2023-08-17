class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        def atmost(k):
            
            l=0
            ans=0
            
            res=0
            for r in range(n):
                k-=nums[r]
                
                while l<=r and k<0:
                    k+=nums[l]
                    l+=1
                res+=(r-l+1)
            return res
        
        return atmost(goal)-atmost(goal-1)