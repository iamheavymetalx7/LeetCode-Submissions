class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast,slow=2,2
        
        while fast<len(nums):
            if nums[slow-2]!=nums[fast]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        # print(nums)
        return slow