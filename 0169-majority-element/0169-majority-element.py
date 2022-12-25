class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        major=0
        
        for i in range(0,len(nums)):
            if cnt==0:
                major=nums[i]
            
            if major==nums[i]:
                cnt+=1
            else:
                cnt-=1
        
        return major
        