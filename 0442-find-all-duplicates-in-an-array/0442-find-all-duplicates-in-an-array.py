class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        
        while i<n:
            correct = nums[i]-1
            
            if nums[correct]!=nums[i]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i+=1
        
        ans=[]
        
        for i,ele in enumerate(nums):
            if ele!=i+1:
                ans.append(ele)
        
        return ans