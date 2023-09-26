class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        
        s =0
        
        even,odd = 0,0
        
        ans =0
        MOD = int(1e9)+7
        
        
        for i in range(n):
            s+=nums[i]
            
            if s&1:
                ans+=even+1
                ans%=MOD
                odd+=1
            else:
                ans+=odd
                ans%=MOD
                even+=1
        return ans