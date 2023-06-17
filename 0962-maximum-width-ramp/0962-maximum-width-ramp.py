class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr=[]
        
        for i,el in enumerate(nums):
            arr.append([el,i])
        
        n=len(nums)
        
        mn=n
        ans=0
        
        
        arr.sort()

        for i in range(n) :
            ans= max(ans,arr[i][1]-mn)
            mn = min(mn,arr[i][1])
        
        return ans
                
            