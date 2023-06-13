class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i=0
        n=len(nums)
        while i<n:
            
            correct = nums[i]-1
            
            if nums[correct]!=nums[i]:
                nums[correct],nums[i] = nums[i],nums[correct]
                
            else:
                i+=1
        ans=[]
        
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(i+1)
                
        
        return ans