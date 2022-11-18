class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_multi =[1]*len(nums)
        postfix_multi=[1]*len(nums)
        
        n=len(nums)
        
        for i in range(1,n):
            prefix_multi[i]=prefix_multi[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            postfix_multi[j] = postfix_multi[j+1]*nums[j+1]
            
        
        ans=[0]*n
        for i in range(n):
            ans[i]=postfix_multi[i]*prefix_multi[i]
        
        return ans