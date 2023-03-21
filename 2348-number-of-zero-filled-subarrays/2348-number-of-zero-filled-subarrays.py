from collections import defaultdict
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        res=0
        
        for ele in nums:
            if ele!=0:
                c=0
            else:
                c+=1
                res+=c
        return res
        