        
'''
Find a mid element = (low+high)/2
if mid is even and If A[mid]!=A[mid+1] then it means that the unique element is left part of the array/ Or if they are same then its in right part of the array.
Similarly A[odd] == A[odd-1] then its in right part.
With just the above statment we can reduce the search space at every step by half.
If A[i]!=A[i-1] && A[i]!=A[i+1] return i;

'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l=0
        r=len(nums)-1
        
        n=len(nums)
        
        if n==1:
            return nums[0]

        if nums[0]!=nums[1]:
            return nums[0]
        
        if nums[r]!=nums[r-1]:
            return nums[r]
        
        while l<=r:
            m=(l+r)//2
            if nums[(m-1)]!=nums[m] and nums[(m+1)]!=nums[m]:
                return nums[m]
            
            elif (m%2==0 and nums[m]==nums[m+1]) or (m%2!=0 and nums[m]==nums[m-1]):
                l=m+1
            else:
                r=m-1
        
        return nums[r]
                
        