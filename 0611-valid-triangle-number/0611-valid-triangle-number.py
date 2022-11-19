class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        ## [a--------b------c] we have now like this case, then note that
        ## since c>=b and c>=a, the cases c+a>b and c+b>a are trivially satisfied
        #therefore we only need to check the case that a+b>c
        
        nums.sort()
        n=len(nums)
        ans=0
        for i in range(n-1,1,-1):
            k=i-1
            j=0
            while j<k:
                if nums[j]+nums[k]>nums[i]:
                    ans+=k-j
                    k-=1
                else:
                    j=j+1
        return ans