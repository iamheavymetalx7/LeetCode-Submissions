class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        n=len(nums)
        arr=[0]*(n)
        
        i=n-1
        j=0
        
        for j in range(1,n,2):
            arr[j]=nums[i]
            i-=1
        
        for j in range(0,n,2):
            arr[j]=nums[i]
            i-=1
        
        nums[:]=arr[:]