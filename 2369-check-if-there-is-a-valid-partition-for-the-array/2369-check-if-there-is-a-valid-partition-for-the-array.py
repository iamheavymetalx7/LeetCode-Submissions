class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        n=len(nums)
        
        def check(x):
            if nums[x+1]-nums[x]==1 and nums[x+2]-nums[x+1]==1:
                return True
            return False
        
        @cache
        def recur(i):
            if i==n:
                return True
            
            
            ans=False
            if i+1<n and nums[i]==nums[i+1]:
                ans |= recur(i+2)
            if i+2<n and nums[i]==nums[i+1] and nums[i+1]==nums[i+2]:
                ans |= recur(i+3)
            if i+2<n and check(i):
                ans|= recur(i+3)
            return ans
        
        return recur(0)
            
        