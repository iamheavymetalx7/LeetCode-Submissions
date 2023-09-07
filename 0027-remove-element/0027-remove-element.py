class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i=0
        j=0
        cnt = nums.count(val)
        while i<len(nums)-cnt:
            if nums[i]==val:
                while j<len(nums) and nums[j]==val:
                    j+=1
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j+=1
        return len(nums)-cnt