class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        n=len(nums)
        ans=0
        
        for i in range(1,n+1):
            ans=max(ans,nums[i-1])
            cur=0
            for j in range(1,102):
                
                ind = j*j*i
                if ind<=n:
                    cur+=nums[ind-1]
                else:
                    ans=max(ans,cur)
                    break

        return ans