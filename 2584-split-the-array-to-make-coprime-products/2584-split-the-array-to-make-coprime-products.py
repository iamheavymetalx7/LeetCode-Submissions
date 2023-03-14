import math
class Solution:
    
    def findValidSplit(self, nums: List[int]) -> int:
        N=len(nums)
        left=1
        i=0
        while i<N-1:
            left*=nums[i]
            j=i+1
            while j<N and math.gcd(left,nums[j])==1:
                j+=1
            if j==N:
                return i
            
            left*=math.prod(nums[i+1:j])
            i=j
        return -1
                