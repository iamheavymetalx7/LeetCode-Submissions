'''
idea: 1. no need to replace the last element
2. we iterate backward in order to get the min elements split
3. if nums[i]%nums[i+1] ==0 then each num_el = nums[i]//nums[i+1] and operations=num_el -1 and update ith to 
nums[i] = nums[i]//num_el

else num_el = nums[i] //nums[i+1] +1
and  operations=num_el -1 and update ith to
nums[i] = nums[i]//nums_el

'''
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                if nums[i]%nums[i+1]==0:
                    ops= (nums[i]//nums[i+1])
                    operations+=ops-1
                    
                    nums[i]=nums[i] //(ops)
                else:
                    ops = (nums[i]//nums[i+1])+1
                    operations+=ops-1
                    nums[i] = nums[i]//ops
        
        return operations