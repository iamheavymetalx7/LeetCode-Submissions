class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr=[]
        nums.sort()
        n=len(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                left=j+1
                right=n-1
                
                while left<right:
                    fourSum=nums[i]+nums[j]+nums[left]+nums[right]       
                    
                    if fourSum==target:
                        arr.append((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif fourSum<target:
                        left+=1
                    else:
                        right-=1
        return arr