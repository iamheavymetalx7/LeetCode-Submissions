class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[-1]*(n-1)
        dp2=[-1]*(n-1)
        
        nums1=nums[0:-1]
        nums2=nums[1:]
        
        if len(nums)==1:
            return nums[0]
        
        
        def recur1(index):
            if index>=n-1:
                return 0
            if dp1[index]!=-1:
                return dp1[index]
            
            dp1[index] = max(recur1(index+2)+nums1[index],recur1(index+1))            
            
            return dp1[index]
            
        def recur2(index):
            if index>=n-1:
                return 0
            if dp2[index]!=-1:
                return dp2[index]
            
            dp2[index] = max(recur2(index+2)+nums2[index],recur2(index+1))            
            
            return dp2[index]
        
        ans1=recur1(0)
        ans2=recur2(0)
        
        return max(ans1,ans2)
    
        