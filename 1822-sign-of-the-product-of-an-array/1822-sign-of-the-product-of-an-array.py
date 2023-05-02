class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sgn=1
        for ele in nums:
            if ele<0:
                sgn*=-1
            elif ele>0:
                sgn*=1
            else:
                sgn=0
                return sgn
        return sgn
        