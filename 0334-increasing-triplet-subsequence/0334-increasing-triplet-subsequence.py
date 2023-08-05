class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        small,big = [int(1e18)]*(2)
        
        
        for n in nums:
            if n<=small:
                small = n
            elif n<=big:
                big =n
            else:
                return True
        return False
        