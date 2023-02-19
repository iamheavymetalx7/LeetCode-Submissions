class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        Sumarr=[0]*n
        Sumarr[0]=nums[0]
        
        for i in range(1,n):
            Sumarr[i]=Sumarr[i-1]+nums[i]
        
        minS=min(0,nums[0])
        
        ans= nums[0]
        
        for i in range(1,n):
            if Sumarr[i]-minS > ans:
                ans=Sumarr[i]-minS
            if Sumarr[i] < minS:
                minS=Sumarr[i]
        return ans
    