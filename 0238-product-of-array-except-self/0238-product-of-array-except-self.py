class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[0]*n
        
        pre[0] = nums[0]
        suff=[0]*n
        
        suff[-1]=nums[-1]
        for i in range(1,n):
            pre[i]=pre[i-1]*nums[i]
        
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]*nums[i]
        
        ans =[0]*n
        
        for i in range(n):
            if i==0:
                ans[i] = suff[i+1]
            elif i==n-1:
                ans[i] = pre[i-1]
            else:
                ans[i]= pre[i-1]*suff[i+1]
        return ans