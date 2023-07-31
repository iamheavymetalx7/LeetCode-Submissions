class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count =1; major = nums[0]
        n=len(nums)
        for i in range(1,n):
            if count==0:
                count+=1
                major= nums[i]
            elif nums[i]==major:
                count+=1
            else:
                count-=1
        
        return (major)
            
        