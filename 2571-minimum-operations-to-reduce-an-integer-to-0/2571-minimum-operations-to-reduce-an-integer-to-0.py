class Solution:
    '''
    # References:
    1. https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/discuss/3204095/*EASIEST-SOLUTION-or-BETTER-THAN-THE-MOST-VOTED-ONE-or-EXPLAINED*
    '''
    def minOperations(self, n: int) -> int:
        pows=[(1<<i) for i in range(int(log2(n))+2)]
        
        ops=0
        
        while n:
            closest=min(pows,key=lambda p: abs(n-p))
            n=abs(n-closest)
            ops+=1

        
        return ops