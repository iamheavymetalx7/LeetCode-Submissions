class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int):
        mx=-1
        mn=-1
        
        for i,num in enumerate(nums):
            if i-indexDifference>=0:
                if mn==-1 or nums[i-indexDifference]<nums[mn]:
                    mn = i-indexDifference
                if mx==-1 or nums[i-indexDifference]>nums[mx]:
                    mx = i-indexDifference
                if num-nums[mn]>= valueDifference:
                    return [mn,i]
                if nums[mx]-num>=valueDifference:
                    return [mx,i]
        return [-1,-1]