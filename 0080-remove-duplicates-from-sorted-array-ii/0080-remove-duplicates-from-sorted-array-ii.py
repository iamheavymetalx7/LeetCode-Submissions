class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        j=1
        cnt=1
        while j<len(nums):
            if nums[i]==nums[j]:
                if cnt<2:
                    cnt+=1
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
                    j+=1
                else:
                    j+=1
            else:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
                cnt=1
                j+=1
        return i+1
            