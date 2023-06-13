class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        i=0
        
        while i<n:
            correct = nums[i]-1
            
            if nums[correct]!=nums[i]:
                nums[correct],nums[i] = nums[i],nums[correct]
            else:
                i+=1
        
        print(nums)
        
        ans=[]
        for i,ele in enumerate(nums):
            if nums[i]!=i+1:
                ans.append(ele)
                ans.append(i+1)
                
        return ans