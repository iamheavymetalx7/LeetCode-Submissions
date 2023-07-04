class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        arr=[]
        
        nums.sort()
        
        if len(nums)<3 or nums[0]>0:
            return
        
        for i,x in enumerate(nums):
            
            if nums[i]>0:
                break
                
            if i>0 and x==nums[i-1]:
                continue
            
            left,right =i+1, len(nums)-1
            
            while left<right:
                threeSum = x+nums[left]+nums[right]
                
                if threeSum ==0:
                    arr.append([x,nums[left],nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    right-=1
        return arr
                